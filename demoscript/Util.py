# **********************************************************************
#
# Copyright (c) 2003-2014 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

import os
import sys
import getopt
import re
import os
import signal
import time
import subprocess

javaHome = os.environ.get("JAVA_HOME", "")
javaCmd = '"%s"' % os.path.join(javaHome, "bin", "java") if javaHome else "java"

# Locate the top level directory of the demo dist (or the top of the
# source tree for a source dist).
path = [ ".", "..", "../..", "../../..", "../../../.." ]
head = os.path.dirname(sys.argv[0])
if len(head) > 0:
    path = [os.path.join(head, p) for p in path]
path = [os.path.abspath(p) for p in path if os.path.exists(os.path.join(p, "demoscript")) ]
toplevel = path[0]
if os.path.isdir(os.path.join(toplevel, "cpp", "demo")):
    sourcedist = True
else:
    sourcedist = False

sys.path.append(os.path.join(path[0], "scripts"))
import Expect

keepGoing = False
iceHome = None
x64 = False
x86 = False
cpp11 = False
preferIPv4 = False
serviceDir = None
demoErrors = []
tracefile = None
defaultHost = None

#
# Default value of --Ice.Default.Host
#
host = "127.0.0.1"

#
# Echo the commands.
#
debug = False

#
# The NodeJS interpreter is called "nodejs" on some platforms
# (e.g., Ubuntu)
#
nodeCmd = "node"
if "NODE" in os.environ:
    nodeCmd = os.environ["NODE"]
else:
    for path in os.environ["PATH"].split(os.pathsep):
        #
        # Stop if we find "php" in the PATH first.
        #
        if os.path.exists(os.path.join(path, "node")):
            break
        elif os.path.exists(os.path.join(path, "nodejs")):
            nodeCmd = "nodejs"
            break

def getNodeCommand():
    return nodeCmd

def getThirdpartyHome():
    version = getIceVersion()
    if os.environ.get("THIRDPARTY_HOME"):
        return os.environ.get("THIRDPARTY_HOME")
    elif isDarwin():
        if os.path.exists("/Library/Developer/Ice-%s-ThirdParty/lib/db.jar" % version):
            return "/Library/Developer/Ice-%s-ThirdParty/" % version
    elif isWin32():
        import winreg
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\ZeroC\\Ice %s Third Party Packages" % \
                                 version, 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY)
            installDir = os.path.abspath(winreg.QueryValueEx(key, "InstallDir")[0])

            if os.path.exists(installDir):
                return installDir
        except WindowsError as error:
            print(error)
    return None

def getJavaVersion():
    p = subprocess.Popen(javaCmd + " -version", shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    if(p.wait() != 0):
        print(javaCmd + " -version failed:\n" + p.stdout.read().decode('UTF-8').strip())
        sys.exit(1)
    matchVersion = re.compile('java version \"(.*)\"')
    m = matchVersion.match(p.stdout.readline().decode('UTF-8'))
    return m.group(1)

class filereader(Expect.reader):
    def __init__(self, desc, p):
        Expect.reader.__init__(self, desc, p, None)

    def run(self):
        self.keepReading = True
        try:
            while True and self.keepReading == True:
                c = self.p.read(1)
                if not c:
                    time.sleep(0.1)
                    # Refresh position so we don't get stuck at EOF
                    # while the file is still being written
                    # (Does not happen in all Python versions)
                    self.p.seek(self.p.tell())
                    continue

                if c == '\r':continue
                self.cv.acquire()
                try:
                    # Depending on Python version and platform, the value c could be a
                    # string or a bytes object.
                    if type(c) != str:
                        c = c.decode()
                    self.trace(c)
                    self.buf.write(c)
                    self.cv.notify()
                finally:
                    self.cv.release()
            self.p.close()
        except ValueError as e:
            pass
        except IOError as e:
            print(e)

    def stopReading(self):
        self.keepReading = False;

class FileExpect(object):
    def __init__(self, path):

        self.buf = "" # The part before the match
        self.before = "" # The part before the match
        self.after = "" # The part after the match
        self.matchindex = 0 # the index of the matched pattern
        self.match = None # The last match

        self.f = open(path, 'r')
        self.r = filereader(path, self.f)

        # The thread is marked as a daemon thread. This is done so that if
        # an expect script runs off the end of main without kill/wait on each
        # spawned process the script will not hang tring to join with the
        # reader thread. Instead __del__ (below) will be called which
        # terminates and joins with the reader thread.
        self.r.setDaemon(True)
        self.r.start()

    def __del__(self):
        # Terminate and clean up.
        if self.r is not None:
            self.terminate()

    def expect(self, pattern, timeout = 20):
        """pattern is either a string, or a list of string regexp patterns.

           timeout == None expect can block indefinitely.

           timeout == -1 then the default is used.
        """
        if timeout == -1:
            timeout = self.timeout

        if type(pattern) != list:
            pattern = [ pattern ]
        def compile(s):
            if type(s) == str:
                return re.compile(s, re.S)
            return None
        pattern = [ ( p, compile(p) ) for p in pattern ]
        try:
            self.buf, self.before, self.after, self.match, self.matchindex = self.r.match(pattern, timeout)
        except Expect.TIMEOUT as e:
            self.buf = ""
            self.before = ""
            self.after = ""
            self.match = None
            self.matchindex = 0
            raise e
        return self.matchindex

    def terminate(self):
        self.r.stopReading()
        self.r.join()
        self.r = None


def getCppCompiler():
    if not isWin32():
        return ""
    compiler = ""
    if os.environ.get("CPP_COMPILER", "") != "":
        compiler = os.environ["CPP_COMPILER"]
    else:
        config = None
        if os.path.exists(os.path.join(toplevel, "cpp", "config", "Make.rules.mak")):
            config = open(os.path.join(toplevel, "cpp", "config", "Make.rules.mak"), "r")
        elif os.path.exists(os.path.join(toplevel, "config", "Make.rules.mak")):
            config = open(os.path.join(toplevel, "config", "Make.rules.mak"), "r")
        if config != None:
            compiler = re.search("CPP_COMPILER[\t\s]*= ([A-Z0-9]*)", config.read()).group(1)
            if compiler != "VC100" and compiler != "VC110" and compiler != "VC120":
                compiler = ""

        if compiler == "":
            p = subprocess.Popen("cl", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            if not p or not p.stdout:
                print("Cannot detect C++ compiler")
                sys.exit(1)
            l = p.stdout.readline().decode("utf-8").strip()
            if l.find("Version 16") != -1:
                compiler = "VC100"
            elif l.find("Version 17") != -1:
                compiler = "VC110"
            elif l.find("Version 18") != -1:
                compiler = "VC120"
            else:
                print("Cannot detect C++ compiler")
                sys.exit(1)
    return compiler

origenv = {}
def dumpenv():
    print("the following environment variables have been set:")
    for k, v in origenv.items():
        added = os.environ[k][:len(os.environ[k])-len(v)]
        if len(v) > 0:
            if isWin32():
                print("%s=%s%%%s%%" % (k, added, k))
            else:
                print("%s=%s$%s" % (k, added, k))
        else:
                print("%s=%s" % (k, added))

def addenv(var, val):
    global origenv
    if not var in origenv:
        origenv[var] = os.environ.get(var, "")
    if var in os.environ:
        os.environ[var] = "%s%s%s" % (val, os.pathsep, os.environ.get(var, ""))
    else:
        os.environ[var] = val

def configurePaths():

    if iceHome:
        sys.stdout.write("[ using Ice installation from " + iceHome + " ")
        if x64:
            sys.stdout.write("(64bit) ")
        sys.stdout.write("]\n")

    binDir = os.path.join(getIceDir("cpp"), "bin")

    # Always add the bin directory to the PATH, it contains executable
    # which might not be in the compiler/arch bin sub-directory.
    if iceHome != "/usr":
        addenv("PATH", binDir)

    if iceHome:

        # Add compiler sub-directory
        if isWin32():
            subdir = None
            if getMapping() != "py":
                if getCppCompiler() == "VC110":
                    subdir = "vc110"

            if subdir:
                binDir = os.path.join(binDir, subdir)
            if x64:
                binDir = os.path.join(binDir, "x64")

        # Add x64 sub-directory
        if isSolaris() and x64:
            if isSparc():
                binDir = os.path.join(binDir, "sparcv9")
            else:
                binDir = os.path.join(binDir, "amd64")
    else:
        #
        # Add third party home to PATH, to use db_xx tools
        #
        if isWin32():
            addenv("PATH", os.path.join(getThirdpartyHome(), "bin\\x64" if x64 else "bin"))
            if getCppCompiler() == "VC110":
                addenv("PATH", os.path.join(getThirdpartyHome(), "bin\\vc110\\x64" if x64 else "bin\\vc110"))
        elif isDarwin():
            addenv("PATH", os.path.join(getThirdpartyHome(), "bin"))


    if binDir != os.path.join(getIceDir("cpp"), "bin"):
        addenv("PATH", binDir)

    if not iceHome:
        addenv("PATH", os.path.join(getIceDir("cs"), "bin"))

    #
    # On Windows, C# assemblies are found thanks to the .exe.config files.
    #
    if isWin32():
        addenv("DEVPATH", os.path.join(getIceDir("cs"), "Assemblies"))
    else:
        addenv("MONO_PATH", os.path.join(getIceDir("cs"), "Assemblies"))

    #
    # On Windows x64, set PYTHONPATH to python/x64.
    #
    if isWin32() and x64:
        addenv("PYTHONPATH", os.path.join(getIceDir("py"), "python", "x64"))
    else:
        addenv("PYTHONPATH", os.path.join(getIceDir("py"), "python"))

    if isWin32() and x64:
        addenv("RUBYLIB", os.path.join(getIceDir("rb"), "ruby", "x64"))
    else:
        addenv("RUBYLIB", os.path.join(getIceDir("rb"), "ruby"))

    if getMapping() == "js":
        addenv("NODE_PATH", os.path.join(getIceDir("js"), "node_modules" if iceHome else "src"))
        addenv("NODE_PATH", ".")

def getMappingDir(mapping):
    """Get the directory containing the demos for the given mapping."""
    # In the source tree
    if sourcedist:
        return os.path.join(mapping, "demo")
    else:
        return mapping

def getMirrorDir(mapping = None):
    """Get the mirror directory for the current demo in the given mapping."""
    here = os.path.abspath(os.getcwd())

    # Split off the front portion portion
    pref = here[:len(toplevel)]
    assert pref == toplevel
    post = here[len(toplevel) + 1:]

    # In the source tree
    if sourcedist:
        scriptPath = os.sep.join(post.split(os.sep)[2:])
    else:
        scriptPath = os.sep.join(post.split(os.sep)[1:])
    return os.path.join(pref, getMappingDir(mapping), scriptPath)

def getIceDir(subdir = None):
    """Get the top level directory of the ice distribution. If ICE_HOME
       is set we're running the test against a binary
       distribution. Otherwise, we're running the test against a
       source distribution."""
    global iceHome
    if iceHome:
        return iceHome
    elif subdir:
        return os.path.join(toplevel, subdir)
    else:
        return toplevel

def isBinDist():
    getIceDir() != os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def isWin32():
    return sys.platform == "win32"

def isCompactFramework():
    return isWin32() and ("COMPACT" in os.environ and os.environ["COMPACT"] == "yes")

def isSolaris():
    return sys.platform == "sunos5"

def isSparc():
    p = os.popen("uname -p")
    l = p.readline().strip()
    if l == "sparc":
        return True
    else:
        return False

def isAIX():
   return sys.platform in ['aix4', 'aix5']

def isDarwin():
   return sys.platform == "darwin"

def isLinux():
    return sys.platform.startswith("linux")

def isMono():
    return not isWin32()

def isSolaris():
    return sys.platform == "sunos5"

global linuxDistribution

if os.path.isfile("/etc/issue"):
    f = open("/etc/issue", "r")
    issue = f.read()
    f.close()
    if issue.find("Red Hat") != -1:
        linuxDistribution = "RedHat"
    elif issue.find("Amazon Linux") != -1:
        linuxDistribution = "Amazon"
    elif issue.find("CentOS") != -1:
        linuxDistribution = "CentOS"
    elif issue.find("Ubuntu") != -1:
        linuxDistribution = "Ubuntu"
    elif issue.find("SUSE Linux") != -1:
        linuxDistribution = "SUSE LINUX"

def isUbuntu():
    return isLinux() and linuxDistribution and linuxDistribution == "Ubuntu"

def isRhel():
    if isLinux() and linuxDistribution:
        for r in ["RedHat", "Amazon", "CentOS"]:
            if linuxDistribution.find(r) != -1:
                return True
    return False

def isSles():
    return isLinux() and linuxDistribution and linuxDistribution == "SUSE LINUX"

def getMapping():
    """Determine the current mapping based on the cwd."""
    here = os.path.abspath(os.getcwd())
    assert os.path.normcase(here[:len(toplevel)]) == os.path.normcase(toplevel)
    return here[len(toplevel)+1:].split(os.sep)[0]

def runDemos(start, args, demos, num = 0, script = False, root = False):
    global demoErrors
    global keepGoing

    total = len(demos)

    #
    # Run each of the demos.
    #
    index = 0
    for i in demos:
        index = index + 1
        if index < start:
            continue

        i = os.path.normpath(i)
        if root:
            dir = os.path.join(toplevel, i)
        else:
            dir = os.path.join(toplevel, getMappingDir(getMapping()), i)

        if script:
            prefix = "echo \""
            suffix = "\""
        else:
            prefix = ""
            suffix = ""

        sys.stdout.write("\n")
        if(num > 0):
            sys.stdout.write("[" + str(num) + "] ")
        print("%s*** running demo %d/%d in %s%s" % (prefix, index, total, dir, suffix))
        sys.stdout.write("%s*** configuration: " % prefix)
        if len(args.strip()) == 0:
            sys.stdout.write("Default ")
        else:
            sys.stdout.write(args.strip() + " ")
        print(suffix)

        if script:
            print("echo \"*** demo started: `date`\"")
            print("cd %s" % dir)
        else:
            print("*** demo started: " + time.strftime("%x %X"))
            sys.stdout.flush()
            os.chdir(dir)

        if script:
            print("if ! %s %s %s; then" % (sys.executable, os.path.join(dir, "expect.py"), args))
            print("  echo 'demo in %s failed'" % os.path.abspath(dir))
            if not keepGoing:
                print("  exit 1")
            print("fi")
        else:
            status = os.system(sys.executable + ' "' + os.path.join(dir, "expect.py") + '" ' + args)

            if status:
                if(num > 0):
                    sys.stdout.write("[" + str(num) + "] ")
                message = "demo in " + dir + " failed with exit status", status,
                print(message)
                if keepGoing == False:
                    print("exiting")
                    sys.exit(status)
                else:
                    print(" ** Error logged and will be displayed again when suite is completed **")
                    demoErrors.append(message)

def run(demos, protobufDemos = [], root = False):
    def usage():
        print("""usage: %s
        --start=index           Start running the demos at the given demo."
        --loop                  Run the demos in a loop."
        --filter=<regex>        Run all the demos that match the given regex."
        --rfilter=<regex>       Run all the demos that do not match the given regex."
        --protobuf              Run the protobuf demos."
        --debug                 Display debugging information on each demos."
        --trace=<output>        Run the demos with tracing enabled."
        --host=host             Set --Ice.Default.Host=<host>."
        --mode=debug|release    Run the demos with debug or release mode builds (win32 only)."
        --continue              Keep running when a demo fails."
        --ice-home=<path>       Use the binary distribution from the given path."
        --x64                   Binary distribution is 64-bit."
        --x86                   Binary distribution is 32-bit."
        --c++11                 Binary distribution is C++11."
        --preferIPv4            Prefer IPv4 stack (java only)."
        --fast                  Run an abbreviated version of the demos."
        --script                Generate a script to run the demos.
        --service-dir=<path>    Directory to locate services for C++Builder/VC6.
        --env                   Dump the environment."
        --noenv                 Do not automatically modify environment.""" % (sys.argv[0]))
        sys.exit(2)

    global keepGoing

    try:
        opts, args = getopt.getopt(sys.argv[1:], "lr:R:", [
                "filter=", "rfilter=", "start=", "loop", "fast", "trace=", "debug", "host=", "mode=",
                "continue", "ice-home=", "x64", "x86", "preferIPv4", "env", "noenv", "script", "protobuf", "service-dir=", "c++11"])
    except getopt.GetoptError:
        usage()

    # Extra args cause a usage error.
    if args:
        usage()

    start = 0
    loop = False
    arg = ""
    filters = []
    script = False
    for o, a in opts:
        if o in ("-l", "--loop"):
            loop = True
        elif o == "--x64":
            global x64
            x64 = True
            arg += " " + o
        elif o == "--x86":
            global x86
            x86 = True
            arg += " " + o
        elif o == "--c++11":
            global cpp11
            cpp11 = True
            arg += " " + o
        elif o == "--preferIPv4":
            global preferIPv4
            preferIPv4 = True
            arg += " " + o
        elif o in ("--env", "--noenv"):
            arg += " " + o
        elif o in ("-c", "--continue"):
            keepGoing = True
        elif o in ("-r", "-R", "--filter", '--rfilter'):
            if o in ("--rfilter", "-R"):
                filters.append((re.compile(a), True))
            else:
                filters.append((re.compile(a), False))
        elif o in ("--host", "--fast", "--trace", "--debug", "--mode", "--ice-home"):
            if o == "--mode":
                if a not in ( "debug", "release"):
                    usage()
            arg += " " + o
            if len(a) > 0:
                arg += " " + a
        elif o in '--start':
            start = int(a)
        elif o in '--script':
            script = True
        elif o in '--protobuf':
            demos = demos + protobufDemos
        elif o in '--service-dir':
            global serviceDir
            serviceDir = a

    for demoFilter, removeFilter in filters:
        if removeFilter:
            demos = [ x for x in demos if not demoFilter.search(x) ]
        else:
            demos = [ x for x in demos if demoFilter.search(x) ]

    if loop:
        num = 1
        while 1:
            runDemos(start, arg, demos, num, script = script, root = root)
            num += 1
    else:
        runDemos(start, arg, demos, script = script, root = root)

    if len(demoErrors) > 0:
        print("The following errors occurred:")
        for x in demoErrors:
            print(x)

def guessBuildModeForDir(cwd):
    import glob
    debugDll = glob.glob(os.path.join(cwd, "*d.dll"))
    # *.dll includes d.dll, so do an intersection on the set.
    dll = [p for p in glob.glob(os.path.join(cwd, "*.dll")) if not p in debugDll ]
    if len(debugDll) > 0 and len(dll) == 0:
        return "debug"
    if len(dll) > 0 and len(debugDll) == 0:
        return "release"
    if len(dll) > 0 and len(debugDll) > 0:
        # Find out which is newer.
        if os.stat(dll[0]).st_ctime > os.stat(debugDll[0]).st_ctime:
            return "release"
        else:
            return "debug"
    return None

def guessBuildMode():
    if not iceHome and sourcedist:
        m = guessBuildModeForDir(os.path.join(toplevel, "cpp", "bin"))
    else:
        m = guessBuildModeForDir(".")
    if m is None:
        raise RuntimeError("cannot guess debug or release mode")
    return m

def isDebugBuild():
    global buildmode
    # Guess the mode, if not set on the command line.
    if not isWin32():
        return False
    if buildmode is None:
        buildmode = guessBuildMode()
        print("(guessed build mode %s)" % buildmode)
    return buildmode == "debug"

def getIceVersion():
    if isWin32():
        config = open(os.path.join(toplevel, "config", "Make.common.rules.mak"), "r")
    else:
        config = open(os.path.join(toplevel, "config", "Make.common.rules"), "r")
    return re.search("VERSION[\t\s]*= ([0-9]+\.[0-9]+(\.[0-9]+|b[0-9]*))", config.read()).group(1)

def getServiceDir():
    global serviceDir
    if serviceDir == None:
        if iceHome:
            serviceDir = os.path.join(iceHome, "bin")
        else:
            serviceDir = "C:\\Progra~1\ZeroC\Ice-" + str(getIceVersion()) + "\\bin"
    return serviceDir

def isX86():
    return x86

def isCpp11():
    return cpp11

def getIceBox(mapping = "cpp"):
    if mapping == "cpp":
        iceBox = "icebox"
        if isWin32() and isDebugBuild():
            iceBox += "d"
        elif isLinux():
            if not x64:
                iceBox += "32"
            if cpp11:
                iceBox += "++11"        
        return iceBox
    elif mapping == "cs":
        if isMono():
            # Mono cannot locate icebox in the PATH. This is wrong for a demo dist.
            return os.path.join(getIceDir("cs"), "bin", "iceboxnet.exe")
        else:
            return "iceboxnet.exe"
    assert False

def getIceBoxAdmin():
    return "iceboxadmin"

def getIceGridRegistry():
    return "icegridregistry"

def getIceGridNode():
    return "icegridnode"

def getIceGridAdmin():
    return "icegridadmin"

def getGlacier2Router():
    return "glacier2router"

def spawn(command, cwd = None, mapping = None):
    tokens = command.split(' ')
    desc = tokens[0]
    args = ""
    for arg in tokens[1:len(tokens)]:
        args += " " + arg

    global defaultHost
    if defaultHost:
        command = '%s %s' % (command, defaultHost)
        args = '%s %s' % (args, defaultHost)

    # magic
    knownCommands = [ "icegridnode", "icegridregistry", "icebox", "iceboxd", "icebox32", "icebox++11", "icebox32++11",
                      "icegridadmin", "icestormadmin", "iceboxadmin", "transformdb", "glacier2router" ]
    if mapping == None:
        if desc in knownCommands:
            mapping = "cpp"
        else:
            mapping = getMapping()

    if mapping == "cs":
        if isMono():
            command = "mono " + command
        else:
            command = "./" + command
    elif mapping == "py":
        command = sys.executable + " -u " + command
    elif mapping == "vb":
        command = "./" + command
    elif mapping == "java":

        command = command.replace("java", "java %s" % getJavaLibraryPath(), 1)

        if preferIPv4:
            command = command.replace("java", "java -Djava.net.preferIPv4Stack=true", 1)
        if isSolaris() and x64:
            command = command.replace("java", "java -d64", 1)
        if javaCmd != "java":
            command = command.replace("java", javaCmd, 1)
    elif mapping == "cpp":
        if cwd != None:
            desc = os.path.join(cwd, desc)
        if isWin32():
            if desc.find(".") == -1:
                desc += ".exe"
        command = desc + " " + args

    if isWin32(): # Under Win32 ./ does not work.
        command = command.replace("./", "")
    if debug:
        print('(%s)' % (command))
    return Expect.Expect(command, logfile = tracefile, desc = desc, mapping = mapping, cwd = cwd)

def watch(path):
    return FileExpect(path)

def cleanDbDir(path):
    for filename in [ os.path.join(path, f) for f in os.listdir(path) if f != ".gitignore" and f != "DB_CONFIG"]:
        if os.path.isdir(filename):
            cleanDbDir(filename)
            try:
                os.rmdir(filename)
            except OSError:
                # This might fail if the directory is empty (because
                # it itself contains a .gitignore file.
                pass
        else:
            os.remove(filename)

def getJavaLibraryPath():
    if isWin32():
        if iceHome:
            return "-Djava.library.path=\"%s\" " % os.path.join(iceHome, "bin\\x64" if x64 else "bin")
        else:
            return "-Djava.library.path=\"%s\" " % os.path.join(getThirdpartyHome(), "bin\\x64" if x64 else "bin")
    elif isDarwin():
        return "-Djava.library.path=%s " % os.path.join(iceHome if iceHome else getThirdpartyHome(), "lib")
    elif isRhel() or isSles():
        return "-Djava.library.path=%s " % ("/usr/lib64" if x64 else "/usr/lib")
    elif isUbuntu():
        return "-Djava.library.path=%s " % ("/usr/lib/x86_64-linux-gnu" if x64 else "/usr/lib/i386-linux-gnu")
    return None

def addLdPath(libpath):
    if isWin32():
        addenv("PATH", libpath)
    elif isAIX():
        addenv("LIBPATH", libpath)
    elif isSolaris():
        if x64:
            addenv("LD_LIBRARY_PATH_64", libpath)
        else:
            addenv("LD_LIBRARY_PATH", libpath)
    elif isDarwin():
        addenv("DYLD_LIBRARY_PATH", libpath)
    else:
        addenv("LD_LIBRARY_PATH", libpath)

def getIceBoxClassPath():
    jarSuffix = "-" + getIceVersion() + ".jar"
    javaDir = getIceDir("java")
    s = ""
    for jar in ["ice", "icebox"]:
        if s != "":
            s += os.pathsep
        s += os.path.join(javaDir, "share/java" if javaDir == "/usr" else "lib", jar + jarSuffix)
    return s

def processCmdLine():
    def usage():
        print("usage: " + sys.argv[0] + " --x64 --x86 --preferIPv4 --env --noenv --fast --trace=output --debug --host host --mode=[debug|release] --ice-home=<dir> --service-dir=<dir>", "--c++11")
        sys.exit(2)
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["env", "noenv", "x64", "x86", "preferIPv4", "fast", "trace=", "debug", "host=", "mode=", "ice-home=", "--servicedir=", "c++11"])
    except getopt.GetoptError:
        usage()

    global fast
    global tracefile
    global buildmode
    global x64
    global x86
    global cpp11
    global preferIPv4
    global debug
    global host
    global defaultHost
    global iceHome
    global serviceDir

    fast = False
    trace = False
    buildmode = None
    x64 = False
    x86 = False
    cpp11 = False
    tracefile = None
    env = False
    noenv = False

    for o, a in opts:
        if o == "--debug":
            debug = True
        if o == "--trace":
            if a == "stdout":
                tracefile = sys.stdout
            else:
                tracefile = open(a, "w")
        if o == "--host":
            host = a
        if o == "--env":
            env = True
        if o == "--noenv":
            noenv = True
        if o == "--fast":
            fast = True
        if o == "--x64":
            x64 = True
        if o == "--x86":
            x86 = True
        if o == "--c++11":
            cpp11 = True
        if o == "--preferIPv4":
            preferIPv4 = True
        if o == "--ice-home":
            iceHome = a
        if o == "--service-dir":
            serviceDir = a
        if o == "--mode":
            buildmode = a
            if buildmode != 'debug' and buildmode != 'release':
                usage()

    if host != "":
        defaultHost = " --Ice.Default.Host=%s" % (host)

    if not iceHome and os.environ.get("USE_BIN_DIST", "no") == "yes" or os.environ.get("ICE_HOME", "") != "":
        if os.environ.get("ICE_HOME", "") != "":
            iceHome = os.environ["ICE_HOME"]
        elif isLinux():
            iceHome = "/usr"

    if not x64:
        x64 = isWin32() and os.environ.get("PLATFORM", "").upper() == "X64" or os.environ.get("LP64", "") == "yes"

    if not noenv:
        configurePaths()
    if env:
        dumpenv()

    if iceHome and isWin32() and not buildmode:
        print("Error: please define --mode=debug or --mode=release")
        sys.exit(1)

import inspect
frame = inspect.currentframe().f_back
# Move to the top-most frame in the callback.
while frame.f_back is not None:
    frame = frame.f_back
if os.path.split(frame.f_code.co_filename)[1] == "expect.py":
    # If we're not in the demo directory, chdir to the correct
    # location.
    if not os.path.isabs(sys.argv[0]):
        d = os.path.join(os.getcwd(), sys.argv[0])
    else:
        d = sys.argv[0]
    d = os.path.split(d)[0]
    if os.path.normpath(d) != os.getcwd():
        os.chdir(d)
    processCmdLine()
