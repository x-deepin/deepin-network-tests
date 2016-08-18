#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import time
import unittest

import accounts
import utils
import utils_dbus

from dbus_gen.com_deepin_daemon_Network import Network
from dbus_gen.com_deepin_daemon_Network_ConnectionSession import ConnectionSession

dbus_network = Network('com.deepin.daemon.Network', '/com/deepin/daemon/Network')

class TestNetworkVpnOpenVpnPassword(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.run_make_cmd("start-service-vpn-openvpn-password")

    @classmethod
    def tearDownClass(cls):
        utils.run_make_cmd("stop-service-vpn-openvpn-password")
        pass

    def test_backend(self):
        session_path = utils_dbus.create_connection('vpn-openvpn', '/')
        dbus_session = ConnectionSession('com.deepin.daemon.Network', session_path)
        uuid = dbus_session.Uuid
        dbus_session.SetKey('alias-vpn-openvpn', 'connection-type', json.dumps('password'))
        dbus_session.SetKey('alias-vpn-openvpn', 'remote', json.dumps(utils.get_ansible_server_host()))
        dbus_session.SetKey('alias-vpn-openvpn', 'username', json.dumps(accounts.vpn_openvpn_username))
        dbus_session.SetKey('alias-vpn-openvpn', 'password', json.dumps(accounts.vpn_openvpn_password))
        dbus_session.SetKey('alias-vpn-openvpn', 'ca', json.dumps(accounts.vpn_openvpn_cacert))
        ok = dbus_session.Save()
        self.assertTrue(ok)
        path = dbus_network.ActivateConnection(uuid, "/")
        self.assertIsNotNone(path)
        time.sleep(5) # wait for connection connected
        self.assertTrue(utils_dbus.is_connection_connected(uuid))
        dbus_network.DeactivateConnection(uuid)
        dbus_network.DeleteConnection(uuid)

    def test_frontend(self):
        # TODO
        pass

if __name__ == '__main__':
    unittest.main()
