#!/bin/sh

set -e

# enable IP forwarding
sysctl -w net.ipv4.ip_forward=1

# configure firewall
iptables -t nat -A POSTROUTING -s 10.99.99.0/24 ! -d 10.99.99.0/24 -j MASQUERADE
iptables -A FORWARD -s 10.99.99.0/24 -p tcp -m tcp --tcp-flags FIN,SYN,RST,ACK SYN -j TCPMSS --set-mss 1356

# generate a new certs/server.crt with the server IP address to avoid strongSwan connecting failed
cd /etc/ipsec.d/
ipsec pki --pub --in private/server.key --type rsa | ipsec pki --issue --lifetime 3650 --cacert cacerts/ca.crt --cakey private/ca.key --dn "C=CH, O=strongSwan, CN=server cert" --san $IPADDRESS --flag serverAuth --flag ikeIntermediate --outform pem > certs/server.crt

exec "$@"
