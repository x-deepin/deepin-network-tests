#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import time

from dbus_gen.com_deepin_daemon_Network import Network
from dbus_gen.com_deepin_daemon_Network_ConnectionSession import ConnectionSession

dbus_network = Network('com.deepin.daemon.Network', '/com/deepin/daemon/Network')

def get_network_devices():
    return json.loads(dbus_network.Devices)
    
def get_active_connections():
    return json.loads(dbus_network.ActiveConnections)

def get_default_wireless_device():
    devices = get_network_devices()
    wireless_devices = devices.get('wireless')
    if wireless_devices and len(wireless_devices) > 0:
        return wireless_devices[0]['Path']
    else:
        return None

def create_connection(conn_type, device_path):
    return dbus_network.CreateConnection(conn_type, device_path)

def is_connection_connected(uuid):
    active_connections = get_active_connections()
    for active_path, active_value in active_connections.items():
        if active_value.get('Uuid') == uuid:
            return True
    return False

def test_active_connection(testcase, uuid, device_path):
    path = dbus_network.ActivateConnection(uuid, "/")
    testcase.assertIsNotNone(path)
    time.sleep(5) # wait for connection connected
    testcase.assertTrue(is_connection_connected(uuid))
    dbus_network.DeactivateConnection(uuid)
    dbus_network.DeleteConnection(uuid)
    time.sleep(5) # wait for connection deleted
