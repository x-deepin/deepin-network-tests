#!/bin/bash

# com.deepin.daemon.Network
dbus-send --type=method_call --print-reply --dest=com.deepin.daemon.Network /com/deepin/daemon/Network org.freedesktop.DBus.Introspectable.Introspect | sed 1d | sed -e '1s/^   string "//' | sed '$s/"$//' > ./dbus_dde_daemon_network.xml
python -m dbus2any -t pydbusclient.tpl -x ./dbus_dde_daemon_network.xml > com_deepin_daemon_Network.py

# com.deepin.daemon.ConnectionSession
session_path=$(dbus-send --type=method_call --print-reply --dest=com.deepin.daemon.Network /com/deepin/daemon/Network com.deepin.daemon.Network.CreateConnection string:"vpn-openvpn" objpath:"/" | sed 1d | sed -e 's/   object path "//' | sed -e 's/"$//')
dbus-send --type=method_call --print-reply --dest=com.deepin.daemon.Network ${session_path} org.freedesktop.DBus.Introspectable.Introspect | sed 1d | sed -e '1s/^   string "//' | sed '$s/"$//' > ./dbus_dde_daemon_network_connectionsession.xml
python -m dbus2any -t pydbusclient.tpl -x ./dbus_dde_daemon_network_connectionsession.xml > com_deepin_daemon_Network_ConnectionSession.py
dbus-send --type=method_call --print-reply --dest=com.deepin.daemon.Network ${session_path} com.deepin.daemon.ConnectionSession.Close

if [ $? -ne 0 ]; then
  echo "run 'sudo pip3 install dbus2any' and Fix dbus2any templates missing issue manually"
  echo "  sudo mkdir /usr/lib/python3.5/site-packages/dbus2any/templates"
  echo "  curl https://raw.githubusercontent.com/hugosenari/dbus2any/master/dbus2any/templates/pydbusclient.tpl | sudo tee /usr/lib/python3.5/site-packages/dbus2any/templates/pydbusclient.tpl"
else
  echo 'Done'
fi
