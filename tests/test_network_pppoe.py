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

class TestNetworkPppoe(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        utils.run_make_cmd("start-service-pppoe")

    @classmethod
    def tearDownClass(cls):
        utils.run_make_cmd("stop-service-pppoe")
        pass

    def test_backend(self):
        session_path = utils_dbus.create_connection('pppoe', '/')
        dbus_session = ConnectionSession('com.deepin.daemon.Network', session_path)
        uuid = dbus_session.Uuid
        dbus_session.SetKey('pppoe', 'username', json.dumps(accounts.pppoe_username))
        dbus_session.SetKey('pppoe', 'password', json.dumps(accounts.pppoe_password))
        self.assertTrue(dbus_session.Save())
        utils_dbus.test_active_connection(self, uuid, utils_dbus.get_default_wired_device())

if __name__ == '__main__':
    unittest.main(verbosity=2)
