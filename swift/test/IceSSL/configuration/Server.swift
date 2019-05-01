//
// Copyright (c) ZeroC, Inc. All rights reserved.
//

import Ice
import TestCommon
import Foundation

class Server: TestHelperI {
    public override func run(args: [String]) throws {
        var restArgs = args
        let communicator = try initialize(args)
        defer {
            communicator.destroy()
        }
        let path = "\(Bundle.main.bundlePath)/Contents/Frameworks/IceSSLConfiguration.bundle/Contents/Resources/certs"
        communicator.getProperties().setProperty(key: "TestAdapter.Endpoints",
                                                 value: getTestEndpoint(num: 0, prot: "tcp"))
        let adapter = try communicator.createObjectAdapter("TestAdapter")
        _ = try adapter.add(servant: ServerFactoryI(defaultDir: path, helper: self),
                            id: Ice.stringToIdentity("factory"))
        try adapter.activate()
        communicator.waitForShutdown()
    }
}
