#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import unittest

import accounts
import utils
import utils_dbus

from dbus_gen.com_deepin_daemon_Network import Network
from dbus_gen.com_deepin_daemon_Network_ConnectionSession import ConnectionSession

dbus_network = Network('com.deepin.daemon.Network', '/com/deepin/daemon/Network')

class TestNetworkVpnOpenconnectCert(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.run_make_cmd("start-service-vpn-openconnect-cert")

    @classmethod
    def tearDownClass(cls):
        utils.run_make_cmd("stop-service-vpn-openconnect-cert")

    def test_backend(self):
        session_path = utils_dbus.create_connection('vpn-openconnect', '/')
        dbus_session = ConnectionSession('com.deepin.daemon.Network', session_path)
        uuid = dbus_session.Uuid
        dbus_session.SetKey('alias-vpn-openconnect', 'gateway', json.dumps(utils.get_ansible_server_host()))
        dbus_session.SetKey('alias-vpn-openconnect', 'cacert', json.dumps(accounts.vpn_openconnect_cert_cacert))
        dbus_session.SetKey('alias-vpn-openconnect', 'usercert', json.dumps(accounts.vpn_openconnect_cert_clientcert))
        dbus_session.SetKey('alias-vpn-openconnect', 'userkey', json.dumps(accounts.vpn_openconnect_cert_clientkey))
        self.assertTrue(dbus_session.Save())
        utils_dbus.test_active_connection(self, uuid, "/")

class TestNetworkVpnOpenconnectPlain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.run_make_cmd("start-service-vpn-openconnect-plain")

    @classmethod
    def tearDownClass(cls):
        utils.run_make_cmd("stop-service-vpn-openconnect-plain")

    # TODO
    @unittest.skip("openconnect/plain needs popup auth dialog to enter username/password")
    def test_backend(self):
        session_path = utils_dbus.create_connection('vpn-openconnect', '/')
        dbus_session = ConnectionSession('com.deepin.daemon.Network', session_path)
        uuid = dbus_session.Uuid
        dbus_session.SetKey('alias-vpn-openconnect', 'gateway', json.dumps(utils.get_ansible_server_host()))
        dbus_session.SetKey('alias-vpn-openconnect', 'cacert', json.dumps(accounts.vpn_openconnect_cert_cacert))
        self.assertTrue(dbus_session.Save())
        utils_dbus.test_active_connection(self, uuid, "/")

if __name__ == '__main__':
    unittest.main(verbosity=2)
