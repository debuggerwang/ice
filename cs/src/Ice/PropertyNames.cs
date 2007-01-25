// **********************************************************************
//
// Copyright (c) 2003-2006 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************

// Generated by makeprops.py from file `/Users/matthew/cvs/ice/config/PropertyNames.def', Thu Jan 25 18:26:49 2007

// IMPORTANT: Do not edit this file -- any edits made here will be lost!

namespace IceInternal
{
    public sealed class PropertyNames
    {
        public static string[] IceProps =
        {
            @"^Ice\.ACM\.Client$",
            @"^Ice\.ACM\.Server$",
            @"^Ice\.AllowableEndpoints$",
            @"^Ice\.BatchAutoFlush$",
            @"^Ice\.ChangeUser$",
            @"^Ice\.Compression\.Level$",
            @"^Ice\.Config$",
            @"^Ice\.Default\.CollocationOptimization$",
            @"^Ice\.Default\.Host$",
            @"^Ice\.Default\.Locator$",
            @"^Ice\.Default\.Locator\.EndpointSelection$",
            @"^Ice\.Default\.Locator\.ConnectionCached$",
            @"^Ice\.Default\.Locator\.PreferSecure$",
            @"^Ice\.Default\.Locator\.LocatorCacheTimeout$",
            @"^Ice\.Default\.Locator\.Locator$",
            @"^Ice\.Default\.Locator\.Router$",
            @"^Ice\.Default\.Locator\.CollocationOptimization$",
            @"^Ice\.Default\.LocatorCacheTimeout$",
            @"^Ice\.Default\.Package$",
            @"^Ice\.Default\.PreferSecure$",
            @"^Ice\.Default\.Protocol$",
            @"^Ice\.Default\.Router$",
            @"^Ice\.Default\.Router\.EndpointSelection$",
            @"^Ice\.Default\.Router\.ConnectionCached$",
            @"^Ice\.Default\.Router\.PreferSecure$",
            @"^Ice\.Default\.Router\.LocatorCacheTimeout$",
            @"^Ice\.Default\.Router\.Locator$",
            @"^Ice\.Default\.Router\.Router$",
            @"^Ice\.Default\.Router\.CollocationOptimization$",
            @"^Ice\.GC\.Interval$",
            @"^Ice\.ImplicitContext$",
            @"^Ice\.InitPlugins$",
            @"^Ice\.LoggerPlugin$",
            @"^Ice\.MessageSizeMax$",
            @"^Ice\.MonitorConnections$",
            @"^Ice\.Nohup$",
            @"^Ice\.NullHandleAbort$",
            @"^Ice\.OA\.[^\s]+\.AdapterId$",
            @"^Ice\.OA\.[^\s]+\.Endpoints$",
            @"^Ice\.OA\.[^\s]+\.Locator$",
            @"^Ice\.OA\.[^\s]+\.PublishedEndpoints$",
            @"^Ice\.OA\.[^\s]+\.RegisterProcess$",
            @"^Ice\.OA\.[^\s]+\.ReplicaGroupId$",
            @"^Ice\.OA\.[^\s]+\.Router$",
            @"^Ice\.OA\.[^\s]+\.ThreadPool\.Size$",
            @"^Ice\.OA\.[^\s]+\.ThreadPool\.SizeMax$",
            @"^Ice\.OA\.[^\s]+\.ThreadPool\.SizeWarn$",
            @"^Ice\.OA\.[^\s]+\.ThreadPool\.StackSize$",
            @"^Ice\.Override\.Compress$",
            @"^Ice\.Override\.ConnectTimeout$",
            @"^Ice\.Override\.Timeout$",
            @"^Ice\.Override\.Secure$",
            @"^Ice\.Package\.[^\s]+$",
            @"^Ice\.Plugin\.[^\s]+$",
            @"^Ice\.PluginLoadOrder$",
            @"^Ice\.PrintAdapterReady$",
            @"^Ice\.PrintProcessId$",
            @"^Ice\.ProgramName$",
            @"^Ice\.RetryIntervals$",
            @"^Ice\.ServerId$",
            @"^Ice\.ServerIdleTime$",
            @"^Ice\.StdErr$",
            @"^Ice\.StdOut$",
            @"^Ice\.ThreadPerConnection$",
            @"^Ice\.ThreadPerConnection\.StackSize$",
            @"^Ice\.ThreadPool\.Client\.Size$",
            @"^Ice\.ThreadPool\.Client\.SizeMax$",
            @"^Ice\.ThreadPool\.Client\.SizeWarn$",
            @"^Ice\.ThreadPool\.Client\.StackSize$",
            @"^Ice\.ThreadPool\.Server\.Size$",
            @"^Ice\.ThreadPool\.Server\.SizeMax$",
            @"^Ice\.ThreadPool\.Server\.SizeWarn$",
            @"^Ice\.ThreadPool\.Server\.StackSize$",
            @"^Ice\.Trace\.GC$",
            @"^Ice\.Trace\.Location$",
            @"^Ice\.Trace\.Network$",
            @"^Ice\.Trace\.Protocol$",
            @"^Ice\.Trace\.Retry$",
            @"^Ice\.Trace\.Slicing$",
            @"^Ice\.UDP\.RcvSize$",
            @"^Ice\.UDP\.SndSize$",
            @"^Ice\.UseEventLog$",
            @"^Ice\.UseSyslog$",
            @"^Ice\.Warn\.AMICallback$",
            @"^Ice\.Warn\.Connections$",
            @"^Ice\.Warn\.Datagrams$",
            @"^Ice\.Warn\.Dispatch$",
            @"^Ice\.Warn\.Endpoints$",
            @"^Ice\.CacheMessageBuffers$",
            null
        };

        public static string[] IceBoxProps =
        {
            @"^IceBox\.InstanceName$",
            @"^IceBox\.LoadOrder$",
            @"^IceBox\.PrintServicesReady$",
            @"^IceBox\.Service\.[^\s]+$",
            @"^IceBox\.ServiceManager\.AdapterId$",
            @"^IceBox\.ServiceManager\.ReplicaGroupId$",
            @"^IceBox\.ServiceManager\.Endpoints$",
            @"^IceBox\.ServiceManager\.PublishedEndpoints$",
            @"^IceBox\.ServiceManager\.RegisterProcess$",
            @"^IceBox\.ServiceManager\.ThreadPool\.Size$",
            @"^IceBox\.ServiceManager\.ThreadPool\.SizeMax$",
            @"^IceBox\.ServiceManager\.ThreadPool\.SizeWarn$",
            @"^IceBox\.ServiceManager\.ThreadPool\.StackSize$",
            @"^IceBox\.UseSharedCommunicator\.[^\s]+$",
            @"^IceBox\.InheritContainerProperties$",
            null
        };

        public static string[] IceGridAdminProps =
        {
            @"^IceGridAdmin\.AuthenticateUsingSSL$",
            @"^IceGridAdmin\.Routed$",
            @"^IceGridAdmin\.Username$",
            @"^IceGridAdmin\.Password$",
            @"^IceGridAdmin\.Trace\.Observers$",
            @"^IceGridAdmin\.Trace\.SaveToRegistry$",
            null
        };

        public static string[] IceGridProps =
        {
            @"^IceGrid\.AdminGUI\.Endpoints$",
            @"^IceGrid\.InstanceName$",
            @"^IceGrid\.Node\.AdapterId$",
            @"^IceGrid\.Node\.ReplicaGroupId$",
            @"^IceGrid\.Node\.RegisterProcess$",
            @"^IceGrid\.Node\.CollocateRegistry$",
            @"^IceGrid\.Node\.Data$",
            @"^IceGrid\.Node\.DisableOnFailure$",
            @"^IceGrid\.Node\.Endpoints$",
            @"^IceGrid\.Node\.Name$",
            @"^IceGrid\.Node\.Output$",
            @"^IceGrid\.Node\.PrintServersReady$",
            @"^IceGrid\.Node\.PropertiesOverride$",
            @"^IceGrid\.Node\.PublishedEndpoints$",
            @"^IceGrid\.Node\.RedirectErrToOut$",
            @"^IceGrid\.Node\.ThreadPool\.Size$",
            @"^IceGrid\.Node\.ThreadPool\.SizeMax$",
            @"^IceGrid\.Node\.ThreadPool\.SizeWarn$",
            @"^IceGrid\.Node\.ThreadPool\.StackSize$",
            @"^IceGrid\.Node\.Trace\.Activator$",
            @"^IceGrid\.Node\.Trace\.Adapter$",
            @"^IceGrid\.Node\.Trace\.Patch$",
            @"^IceGrid\.Node\.Trace\.Replica$",
            @"^IceGrid\.Node\.Trace\.Server$",
            @"^IceGrid\.Node\.UserAccounts$",
            @"^IceGrid\.Node\.UserAccountMapper$",
            @"^IceGrid\.Node\.WaitTime$",
            @"^IceGrid\.Registry\.SessionManager\.AdapterId$",
            @"^IceGrid\.Registry\.SessionManager\.ReplicaGroupId$",
            @"^IceGrid\.Registry\.SessionManager\.Endpoints$",
            @"^IceGrid\.Registry\.SessionManager\.PublishedEndpoints$",
            @"^IceGrid\.Registry\.SessionManager\.RegisterProcess$",
            @"^IceGrid\.Registry\.SessionManager\.ThreadPool\.Size$",
            @"^IceGrid\.Registry\.SessionManager\.ThreadPool\.SizeMax$",
            @"^IceGrid\.Registry\.SessionManager\.ThreadPool\.SizeWarn$",
            @"^IceGrid\.Registry\.SessionManager\.ThreadPool\.StackSize$",
            @"^IceGrid\.Registry\.AdminCryptPasswords$",
            @"^IceGrid\.Registry\.AdminPermissionsVerifier$",
            @"^IceGrid\.Registry\.AdminSSLPermissionsVerifier$",
            @"^IceGrid\.Registry\.Client\.AdapterId$",
            @"^IceGrid\.Registry\.Client\.ReplicaGroupId$",
            @"^IceGrid\.Registry\.Client\.Endpoints$",
            @"^IceGrid\.Registry\.Client\.PublishedEndpoints$",
            @"^IceGrid\.Registry\.Client\.RegisterProcess$",
            @"^IceGrid\.Registry\.Client\.ThreadPool\.Size$",
            @"^IceGrid\.Registry\.Client\.ThreadPool\.SizeMax$",
            @"^IceGrid\.Registry\.Client\.ThreadPool\.SizeWarn$",
            @"^IceGrid\.Registry\.Client\.ThreadPool\.StackSize$",
            @"^IceGrid\.Registry\.CryptPasswords$",
            @"^IceGrid\.Registry\.Data$",
            @"^IceGrid\.Registry\.DefaultTemplates$",
            @"^IceGrid\.Registry\.DynamicRegistration$",
            @"^IceGrid\.Registry\.Internal\.AdapterId$",
            @"^IceGrid\.Registry\.Internal\.ReplicaGroupId$",
            @"^IceGrid\.Registry\.Internal\.Endpoints$",
            @"^IceGrid\.Registry\.Internal\.PublishedEndpoints$",
            @"^IceGrid\.Register\.Internal\.RegisterProcess$",
            @"^IceGrid\.Registry\.Internal\.ThreadPool\.Size$",
            @"^IceGrid\.Registry\.Internal\.ThreadPool\.SizeMax$",
            @"^IceGrid\.Registry\.Internal\.ThreadPool\.SizeWarn$",
            @"^IceGrid\.Registry\.Internal\.ThreadPool\.StackSize$",
            @"^IceGrid\.Registry\.NodeSessionTimeout$",
            @"^IceGrid\.Registry\.PermissionsVerifier$",
            @"^IceGrid\.Registry\.ReplicaName$",
            @"^IceGrid\.Registry\.ReplicaSessionTimeout$",
            @"^IceGrid\.Registry\.Server\.AdapterId$",
            @"^IceGrid\.Registry\.Server\.ReplicaGroupId$",
            @"^IceGrid\.Registry\.Server\.Endpoints$",
            @"^IceGrid\.Registry\.Server\.PublishedEndpoints$",
            @"^IceGrid\.Registry\.Server\.RegisterProcess$",
            @"^IceGrid\.Registry\.Server\.ThreadPool\.Size$",
            @"^IceGrid\.Registry\.Server\.ThreadPool\.SizeMax$",
            @"^IceGrid\.Registry\.Server\.ThreadPool\.SizeWarn$",
            @"^IceGrid\.Registry\.Server\.ThreadPool\.StackSize$",
            @"^IceGrid\.Registry\.SessionTimeout$",
            @"^IceGrid\.Registry\.SSLPermissionsVerifier$",
            @"^IceGrid\.Registry\.Trace\.Application$",
            @"^IceGrid\.Registry\.Trace\.Adapter$",
            @"^IceGrid\.Registry\.Trace\.Locator$",
            @"^IceGrid\.Registry\.Trace\.Node$",
            @"^IceGrid\.Registry\.Trace\.Object$",
            @"^IceGrid\.Registry\.Trace\.Patch$",
            @"^IceGrid\.Registry\.Trace\.Replica$",
            @"^IceGrid\.Registry\.Trace\.Server$",
            @"^IceGrid\.Registry\.Trace\.Session$",
            @"^IceGrid\.Registry\.UserAccounts$",
            null
        };

        public static string[] IcePatch2Props =
        {
            @"^IcePatch2\.AdapterId$",
            @"^IcePatch2\.ReplicaGroupId$",
            @"^IcePatch2\.Admin\.AdapterId$",
            @"^IcePatch2\.Admin\.ReplicaGroupId$",
            @"^IcePatch2\.Admin\.Endpoints$",
            @"^IcePatch2\.Admin\.PublishedEndpoints$",
            @"^IcePatch2\.Admin\.RegisterProcess$",
            @"^IcePatch2\.Admin\.ThreadPool\.Size$",
            @"^IcePatch2\.Admin\.ThreadPool\.SizeMax$",
            @"^IcePatch2\.Admin\.ThreadPool\.SizeWarn$",
            @"^IcePatch2\.Admin\.ThreadPool\.StackSize$",
            @"^IcePatch2\.ChunkSize$",
            @"^IcePatch2\.Directory$",
            @"^IcePatch2\.Endpoints$",
            @"^IcePatch2\.InstanceName$",
            @"^IcePatch2\.PublishedEndpoints$",
            @"^IcePatch2\.RegisterProcess$",
            @"^IcePatch2\.Remove$",
            @"^IcePatch2\.Thorough$",
            @"^IcePatch2\.ThreadPool\.Size$",
            @"^IcePatch2\.ThreadPool\.SizeMax$",
            @"^IcePatch2\.ThreadPool\.SizeWarn$",
            @"^IcePatch2\.ThreadPool\.StackSize$",
            null
        };

        public static string[] IceSSLProps =
        {
            @"^IceSSL\.Alias$",
            @"^IceSSL\.CertAuthDir$",
            @"^IceSSL\.CertAuthFile$",
            @"^IceSSL\.CertFile$",
            @"^IceSSL\.CheckCertName$",
            @"^IceSSL\.CheckCRL$",
            @"^IceSSL\.Ciphers$",
            @"^IceSSL\.DefaultDir$",
            @"^IceSSL\.DH\.[^\s]+$",
            @"^IceSSL\.EntropyDaemon$",
            @"^IceSSL\.FindCert\.[^\s]+$",
            @"^IceSSL\.ImportCert\.[^\s]+$",
            @"^IceSSL\.KeyFile$",
            @"^IceSSL\.Keystore$",
            @"^IceSSL\.KeystorePassword$",
            @"^IceSSL\.KeystoreType$",
            @"^IceSSL\.Password$",
            @"^IceSSL\.PasswordRetryMax$",
            @"^IceSSL\.Protocols$",
            @"^IceSSL\.Random$",
            @"^IceSSL\.Trace\.Security$",
            @"^IceSSL\.Truststore$",
            @"^IceSSL\.TruststorePassword$",
            @"^IceSSL\.TruststoreType$",
            @"^IceSSL\.VerifyDepthMax$",
            @"^IceSSL\.VerifyPeer$",
            @"^IceSSL\.TrustOnly$",
            @"^IceSSL\.TrustOnly\.Client$",
            @"^IceSSL\.TrustOnly\.Server$",
            @"^IceSSL\.TrustOnly\.Server\.[^\s]+$",
            null
        };

        public static string[] IceStormAdminProps =
        {
            @"^IceStormAdmin\.TopicManager\.[^\s]+$",
            null
        };

        public static string[] IceStormProps =
        {
            @"^IceStorm\.Flush\.Timeout$",
            @"^IceStorm\.InstanceName$",
            @"^IceStorm\.Publish\.AdapterId$",
            @"^IceStorm\.Publish\.ReplicaGroupId$",
            @"^IceStorm\.Publish\.Endpoints$",
            @"^IceStorm\.Publish\.PublishedEndpoints$",
            @"^IceStorm\.Publish\.RegisterProcess$",
            @"^IceStorm\.Publish\.ThreadPool\.Size$",
            @"^IceStorm\.Publish\.ThreadPool\.SizeMax$",
            @"^IceStorm\.Publish\.ThreadPool\.SizeWarn$",
            @"^IceStorm\.Publish\.ThreadPool\.StackSize$",
            @"^IceStorm\.TopicManager\.AdapterId$",
            @"^IceStorm\.TopicManager\.ReplicaGroupId$",
            @"^IceStorm\.TopicManager\.Endpoints$",
            @"^IceStorm\.TopicManager\.Proxy$",
            @"^IceStorm\.TopicManager\.PublishedEndpoints$",
            @"^IceStorm\.TopicManager\.RegisterProcess$",
            @"^IceStorm\.TopicManager\.ThreadPool\.Size$",
            @"^IceStorm\.TopicManager\.ThreadPool\.SizeMax$",
            @"^IceStorm\.TopicManager\.ThreadPool\.SizeWarn$",
            @"^IceStorm\.TopicManager\.ThreadPool\.StackSize$",
            @"^IceStorm\.SubscriberPool\.Size$",
            @"^IceStorm\.SubscriberPool\.SizeMax$",
            @"^IceStorm\.SubscriberPool\.SizeWarn$",
            @"^IceStorm\.SubscriberPool\.Timeout$",
            @"^IceStorm\.Trace\.Flush$",
            @"^IceStorm\.Trace\.Subscriber$",
            @"^IceStorm\.Trace\.SubscriberPool$",
            @"^IceStorm\.Trace\.Topic$",
            @"^IceStorm\.Trace\.TopicManager$",
            @"^IceStorm\.Send\.Timeout$",
            @"^IceStorm\.Discard\.Interval$",
            null
        };

        public static string[] Glacier2Props =
        {
            @"^Glacier2\.AddSSLContext$",
            @"^Glacier2\.AddUserToAllowCategories$",
            @"^Glacier2\.Admin\.Endpoints$",
            @"^Glacier2\.Admin\.PublishedEndpoints$",
            @"^Glacier2\.Admin\.RegisterProcess$",
            @"^Glacier2\.AllowCategories$",
            @"^Glacier2\.Client\.AlwaysBatch$",
            @"^Glacier2\.Client\.Buffered$",
            @"^Glacier2\.Client\.Endpoints$",
            @"^Glacier2\.Client\.ForwardContext$",
            @"^Glacier2\.Client\.PublishedEndpoints$",
            @"^Glacier2\.Client\.RegisterProcess$",
            @"^Glacier2\.Client\.SleepTime$",
            @"^Glacier2\.Client\.Trace\.Override$",
            @"^Glacier2\.Client\.Trace\.Reject$",
            @"^Glacier2\.Client\.Trace\.Request$",
            @"^Glacier2\.Filter\.Address\.Reject$",
            @"^Glacier2\.Filter\.Address\.Accept$",
            @"^Glacier2\.Filter\.ProxySizeMax$",
            @"^Glacier2\.Filter\.Category\.Accept$",
            @"^Glacier2\.Filter\.Category\.AcceptUser$",
            @"^Glacier2\.Filter\.AdapterId\.Accept$",
            @"^Glacier2\.Filter\.Identity\.Accept$",
            @"^Glacier2\.CryptPasswords$",
            @"^Glacier2\.InstanceName$",
            @"^Glacier2\.PermissionsVerifier$",
            @"^Glacier2\.PermissionsVerifier\.EndpointSelection$",
            @"^Glacier2\.PermissionsVerifier\.ConnectionCached$",
            @"^Glacier2\.PermissionsVerifier\.PreferSecure$",
            @"^Glacier2\.PermissionsVerifier\.LocatorCacheTimeout$",
            @"^Glacier2\.PermissionsVerifier\.Locator$",
            @"^Glacier2\.PermissionsVerifier\.Router$",
            @"^Glacier2\.PermissionsVerifier\.CollocationOptimization$",
            @"^Glacier2\.ReturnClientProxy$",
            @"^Glacier2\.SSLPermissionsVerifier$",
            @"^Glacier2\.SSLPermissionsVerifier\.EndpointSelection$",
            @"^Glacier2\.SSLPermissionsVerifier\.ConnectionCached$",
            @"^Glacier2\.SSLPermissionsVerifier\.PreferSecure$",
            @"^Glacier2\.SSLPermissionsVerifier\.LocatorCacheTimeout$",
            @"^Glacier2\.SSLPermissionsVerifier\.Locator$",
            @"^Glacier2\.SSLPermissionsVerifier\.Router$",
            @"^Glacier2\.SSLPermissionsVerifier\.CollocationOptimization$",
            @"^Glacier2\.RoutingTable\.MaxSize$",
            @"^Glacier2\.Server\.AlwaysBatch$",
            @"^Glacier2\.Server\.Buffered$",
            @"^Glacier2\.Server\.Endpoints$",
            @"^Glacier2\.Server\.ForwardContext$",
            @"^Glacier2\.Server\.PublishedEndpoints$",
            @"^Glacier2\.Server\.RegisterProcess$",
            @"^Glacier2\.Server\.SleepTime$",
            @"^Glacier2\.Server\.Trace\.Override$",
            @"^Glacier2\.Server\.Trace\.Request$",
            @"^Glacier2\.SessionManager$",
            @"^Glacier2\.SessionManager\.EndpointSelection$",
            @"^Glacier2\.SessionManager\.ConnectionCached$",
            @"^Glacier2\.SessionManager\.PreferSecure$",
            @"^Glacier2\.SessionManager\.LocatorCacheTimeout$",
            @"^Glacier2\.SessionManager\.Locator$",
            @"^Glacier2\.SessionManager\.Router$",
            @"^Glacier2\.SessionManager\.CollocationOptimization$",
            @"^Glacier2\.SSLSessionManager$",
            @"^Glacier2\.SSLSessionManager\.EndpointSelection$",
            @"^Glacier2\.SSLSessionManager\.ConnectionCached$",
            @"^Glacier2\.SSLSessionManager\.PreferSecure$",
            @"^Glacier2\.SSLSessionManager\.LocatorCacheTimeout$",
            @"^Glacier2\.SSLSessionManager\.Locator$",
            @"^Glacier2\.SSLSessionManager\.Router$",
            @"^Glacier2\.SSLSessionManager\.CollocationOptimization$",
            @"^Glacier2\.SessionTimeout$",
            @"^Glacier2\.Trace\.RoutingTable$",
            @"^Glacier2\.Trace\.Session$",
            null
        };

        public static string[] FreezeProps =
        {
            @"^Freeze\.DbEnv\.[^\s]+\.CheckpointPeriod$",
            @"^Freeze\.DbEnv\.[^\s]+\.DbHome$",
            @"^Freeze\.DbEnv\.[^\s]+\.DbPrivate$",
            @"^Freeze\.DbEnv\.[^\s]+\.DbRecoverFatal$",
            @"^Freeze\.DbEnv\.[^\s]+\.OldLogsAutoDelete$",
            @"^Freeze\.DbEnv\.[^\s]+\.PeriodicCheckpointMinSize$",
            @"^Freeze\.Evictor\.[^\s]+\.MaxTxSize$",
            @"^Freeze\.Evictor\.[^\s]+\.SavePeriod$",
            @"^Freeze\.Evictor\.[^\s]+\.SaveSizeTrigger$",
            @"^Freeze\.Evictor\.[^\s]+\.StreamTimeout$",
            @"^Freeze\.Evictor\.[^\s]+\.PopulateEmptyIndices$",
            @"^Freeze\.Evictor\.UseNonmutating$",
            @"^Freeze\.Trace\.DbEnv$",
            @"^Freeze\.Trace\.Evictor$",
            @"^Freeze\.Trace\.Map$",
            @"^Freeze\.Trace\.Transaction$",
            @"^Freeze\.Warn\.CloseInFinalize$",
            @"^Freeze\.Warn\.Deadlocks$",
            null
        };

        public static string[][] validProps =
        {
            IcePatch2Props,
            IceStormProps,
            IceGridAdminProps,
            IceSSLProps,
            IceProps,
            FreezeProps,
            IceGridProps,
            Glacier2Props,
            IceStormAdminProps,
            IceBoxProps,
            null
        };

        public static string[] clPropNames =
        {
            "Ice",
            "IceBox",
            "IceGridAdmin",
            "IceGrid",
            "IcePatch2",
            "IceSSL",
            "IceStormAdmin",
            "IceStorm",
            "Glacier2",
            "Freeze",
            null
        };
    }
}
