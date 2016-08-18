#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import utils

# vpn-l2tp
vpn_l2tp_username = 'test'
vpn_l2tp_password = 'test'

# vpn-l2tp-ipsec
vpn_l2tp_ipsec_key = 'test'

# vpn-openconnect-cert
vpn_openconnect_cert_cacert = utils.get_abs_path() + '/../dockerfiles/vpn-openconnect-cert/etc/ocserv/ca.crt'
vpn_openconnect_cert_clientcert = utils.get_abs_path() + '/../dockerfiles/vpn-openconnect-cert/etc/ocserv/client.crt'
vpn_openconnect_cert_clientkey = utils.get_abs_path() + '/../dockerfiles/vpn-openconnect-cert/etc/ocserv/client.key'

# vpn-openvpn-password
vpn_openvpn_password_cacert = utils.get_abs_path() + '/../dockerfiles/vpn-openvpn-password/etc/openvpn/easy-rsa/pki/ca.crt'
vpn_openvpn_password_username = 'test'
vpn_openvpn_password_password = 'test'

# vpn-openvpn-tls
vpn_openvpn_tls_cacert = utils.get_abs_path() + '/../dockerfiles/vpn-openvpn-tls/etc/openvpn/easy-rsa/pki/ca.crt'
vpn_openvpn_tls_clientcert = utils.get_abs_path() + '/../dockerfiles/vpn-openvpn-tls/etc/openvpn/easy-rsa/pki/issued/client.crt'
vpn_openvpn_tls_clientkey = utils.get_abs_path() + '/../dockerfiles/vpn-openvpn-tls/etc/openvpn/easy-rsa/pki/private/client.key'
vpn_openvpn_tls_clientpass = 'test'
