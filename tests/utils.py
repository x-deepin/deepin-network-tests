#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess

ansible_server_host = None

def run_make_cmd(command):
    os.system('make --no-print-directory -C ' + os.path.dirname(__file__) +  '/../ ' + command)

def run_make_cmd_with_output(command):
    proc = subprocess.Popen(['make', '--no-print-directory', '-C', os.path.dirname(__file__) +  '/../', command], stdout=subprocess.PIPE, universal_newlines=True)
    (out, err) = proc.communicate()
    return out.strip() # remove tailing newlines

def get_abs_path():
    return os.path.dirname(__file__)

def get_ansible_server_host():
    global ansible_server_host
    if ansible_server_host == None:
        ansible_server_host=run_make_cmd_with_output('get-ansible-server-host')
    return ansible_server_host
