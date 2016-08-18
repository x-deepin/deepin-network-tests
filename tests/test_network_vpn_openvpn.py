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
        dbus_session.SetKey('alias-vpn-openvpn', 'username', json.dumps(accounts.vpn_openvpn_password_username))
        dbus_session.SetKey('alias-vpn-openvpn', 'password', json.dumps(accounts.vpn_openvpn_password_password))
        dbus_session.SetKey('alias-vpn-openvpn', 'ca', json.dumps(accounts.vpn_openvpn_password_cacert))
        self.assertTrue(dbus_session.Save())
        utils_dbus.test_active_connection(self, uuid, "/")

    def test_frontend(self):
        # TODO
        pass

class TestNetworkVpnOpenVpnTls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.run_make_cmd("start-service-vpn-openvpn-tls")

    @classmethod
    def tearDownClass(cls):
        utils.run_make_cmd("stop-service-vpn-openvpn-tls")
        pass

    def test_backend(self):
        session_path = utils_dbus.create_connection('vpn-openvpn', '/')
        dbus_session = ConnectionSession('com.deepin.daemon.Network', session_path)
        uuid = dbus_session.Uuid
        dbus_session.SetKey('alias-vpn-openvpn', 'connection-type', json.dumps('tls'))
        dbus_session.SetKey('alias-vpn-openvpn', 'remote', json.dumps(utils.get_ansible_server_host()))
        dbus_session.SetKey('alias-vpn-openvpn', 'ca', json.dumps(accounts.vpn_openvpn_tls_cacert))
        dbus_session.SetKey('alias-vpn-openvpn', 'cert', json.dumps(accounts.vpn_openvpn_tls_clientcert))
        dbus_session.SetKey('alias-vpn-openvpn', 'key', json.dumps(accounts.vpn_openvpn_tls_clientkey))
        dbus_session.SetKey('alias-vpn-openvpn', 'cert-pass', json.dumps(accounts.vpn_openvpn_tls_clientpass))
        self.assertTrue(dbus_session.Save())
        utils_dbus.test_active_connection(self, uuid, "/")

    def test_frontend(self):
        # TODO
        pass

if __name__ == '__main__':
    unittest.main()
