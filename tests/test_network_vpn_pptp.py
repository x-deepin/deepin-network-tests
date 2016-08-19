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

class TestNetworkVpnPptp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.run_make_cmd("start-service-vpn-pptp")

    @classmethod
    def tearDownClass(cls):
        utils.run_make_cmd("stop-service-vpn-pptp")

    def test_backend(self):
        session_path = utils_dbus.create_connection('vpn-pptp', '/')
        dbus_session = ConnectionSession('com.deepin.daemon.Network', session_path)
        uuid = dbus_session.Uuid
        dbus_session.SetKey('alias-vpn-pptp', 'gateway', json.dumps(utils.get_ansible_server_host()))
        dbus_session.SetKey('alias-vpn-pptp', 'user', json.dumps(accounts.vpn_pptp_username))
        dbus_session.SetKey('alias-vpn-pptp', 'password', json.dumps(accounts.vpn_pptp_password))
        self.assertTrue(dbus_session.Save())
        # try to connect/disconnect twice to check reconnect failed issue for vpn-pptp
        utils_dbus.test_active_connection(self, uuid, "/", delete_conn = False)
        utils_dbus.test_active_connection(self, uuid, "/", delete_conn = True)

class TestNetworkVpnPptpNoMppe(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.run_make_cmd("start-service-vpn-pptp-no-mppe")

    @classmethod
    def tearDownClass(cls):
        utils.run_make_cmd("stop-service-vpn-pptp-no-mppe")

    def test_backend(self):
        session_path = utils_dbus.create_connection('vpn-pptp', '/')
        dbus_session = ConnectionSession('com.deepin.daemon.Network', session_path)
        uuid = dbus_session.Uuid
        dbus_session.SetKey('alias-vpn-pptp', 'gateway', json.dumps(utils.get_ansible_server_host()))
        dbus_session.SetKey('alias-vpn-pptp', 'user', json.dumps(accounts.vpn_pptp_username))
        dbus_session.SetKey('alias-vpn-pptp', 'password', json.dumps(accounts.vpn_pptp_password))
        dbus_session.SetKey('alias-vpn-pptp-ppp', 'vk-require-mppe', json.dumps(False))
        self.assertTrue(dbus_session.Save())
        utils_dbus.test_active_connection(self, uuid, "/")

if __name__ == '__main__':
    unittest.main(verbosity=2)
