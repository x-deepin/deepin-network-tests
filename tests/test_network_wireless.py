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

class TestNetworkWirelessWep(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.run_make_cmd("router-save-wireless-settings")
        utils.run_make_cmd("router-setup-wireless-wep")

    @classmethod
    def tearDownClass(cls):
        utils.run_make_cmd("router-restore-wireless-settings")

    def test_backend(self):
        session_path = utils_dbus.create_connection('wireless', '/')
        dbus_session = ConnectionSession('com.deepin.daemon.Network', session_path)
        uuid = dbus_session.Uuid
        dbus_session.SetKey('802-11-wireless', 'ssid', json.dumps(accounts.router_wireless_ssid))
        dbus_session.SetKey('802-11-wireless-security', 'vk-key-mgmt', json.dumps("wep"))
        dbus_session.SetKey('802-11-wireless-security', 'wep-key0', json.dumps(accounts.router_wireless_wep_password))
        self.assertTrue(dbus_session.Save())
        utils_dbus.test_active_connection(self, uuid, utils_dbus.get_default_wireless_device())

class TestNetworkWirelessWpaPsk(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.run_make_cmd("router-save-wireless-settings")
        utils.run_make_cmd("router-setup-wireless-wpa-psk")

    @classmethod
    def tearDownClass(cls):
        utils.run_make_cmd("router-restore-wireless-settings")
        pass

    def test_backend(self):
        session_path = utils_dbus.create_connection('wireless', '/')
        dbus_session = ConnectionSession('com.deepin.daemon.Network', session_path)
        uuid = dbus_session.Uuid
        dbus_session.SetKey('802-11-wireless', 'ssid', json.dumps(accounts.router_wireless_ssid))
        dbus_session.SetKey('802-11-wireless-security', 'vk-key-mgmt', json.dumps("wpa-psk"))
        dbus_session.SetKey('802-11-wireless-security', 'psk', json.dumps(accounts.router_wireless_wpa_psk_password))
        self.assertTrue(dbus_session.Save())
        utils_dbus.test_active_connection(self, uuid, utils_dbus.get_default_wireless_device())

class TestNetworkWirelessWapEap(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.run_make_cmd("start-service-freeradius")
        utils.run_make_cmd("router-save-wireless-settings")
        utils.run_make_cmd("router-setup-wireless-wpa-eap")

    @classmethod
    def tearDownClass(cls):
        utils.run_make_cmd("router-restore-wireless-settings")
        utils.run_make_cmd("stop-service-freeradius")
        pass

    def test_backend_tls(self):
        session_path = utils_dbus.create_connection('wireless', '/')
        dbus_session = ConnectionSession('com.deepin.daemon.Network', session_path)
        uuid = dbus_session.Uuid
        dbus_session.SetKey('802-11-wireless', 'ssid', json.dumps(accounts.router_wireless_ssid))
        dbus_session.SetKey('802-11-wireless-security', 'vk-key-mgmt', json.dumps("wpa-eap"))
        dbus_session.SetKey('802-1x', 'vk-eap', json.dumps("tls"))
        dbus_session.SetKey('802-1x', 'identity', json.dumps(accounts.freeradius_identity))
        dbus_session.SetKey('802-1x', 'vk-ca-cert', json.dumps(accounts.freeradius_cacert))
        dbus_session.SetKey('802-1x', 'vk-client-cert', json.dumps(accounts.freeradius_clientcert))
        dbus_session.SetKey('802-1x', 'vk-private-key', json.dumps(accounts.freeradius_clientkey))
        dbus_session.SetKey('802-1x', 'private-key-password', json.dumps(accounts.freeradius_clientpassword))
        self.assertTrue(dbus_session.Save())
        utils_dbus.test_active_connection(self, uuid, utils_dbus.get_default_wireless_device())

    def test_backend_ttls(self):
        session_path = utils_dbus.create_connection('wireless', '/')
        dbus_session = ConnectionSession('com.deepin.daemon.Network', session_path)
        uuid = dbus_session.Uuid
        dbus_session.SetKey('802-11-wireless', 'ssid', json.dumps(accounts.router_wireless_ssid))
        dbus_session.SetKey('802-11-wireless-security', 'vk-key-mgmt', json.dumps("wpa-eap"))
        dbus_session.SetKey('802-1x', 'vk-eap', json.dumps("ttls"))
        dbus_session.SetKey('802-1x', 'identity', json.dumps(accounts.freeradius_identity))
        dbus_session.SetKey('802-1x', 'vk-ca-cert', json.dumps(accounts.freeradius_cacert))
        dbus_session.SetKey('802-1x', 'password', json.dumps(accounts.freeradius_password))
        self.assertTrue(dbus_session.Save())
        utils_dbus.test_active_connection(self, uuid, utils_dbus.get_default_wireless_device())

    def test_backend_peap(self):
        session_path = utils_dbus.create_connection('wireless', '/')
        dbus_session = ConnectionSession('com.deepin.daemon.Network', session_path)
        uuid = dbus_session.Uuid
        dbus_session.SetKey('802-11-wireless', 'ssid', json.dumps(accounts.router_wireless_ssid))
        dbus_session.SetKey('802-11-wireless-security', 'vk-key-mgmt', json.dumps("wpa-eap"))
        dbus_session.SetKey('802-1x', 'vk-eap', json.dumps("peap"))
        dbus_session.SetKey('802-1x', 'identity', json.dumps(accounts.freeradius_identity))
        dbus_session.SetKey('802-1x', 'vk-ca-cert', json.dumps(accounts.freeradius_cacert))
        dbus_session.SetKey('802-1x', 'password', json.dumps(accounts.freeradius_password))
        self.assertTrue(dbus_session.Save())
        utils_dbus.test_active_connection(self, uuid, utils_dbus.get_default_wireless_device())

if __name__ == '__main__':
    unittest.main(verbosity=2)
