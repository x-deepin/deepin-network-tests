# References:
#   https://github.com/kylemanna/docker-openvpn
#   https://networklessons.com/linux/openvpn-server-usernamepassword-authentication/

FROM ubuntu:16.10

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y iptables openvpn

COPY ./etc/openvpn/openvpn.conf /etc/openvpn/openvpn.conf
COPY ./etc/openvpn/auth-simple.sh /etc/openvpn/auth-simple.sh
COPY ./etc/openvpn/easy-rsa/ /etc/openvpn/easy-rsa/
RUN chmod 0700 /etc/openvpn/auth-simple.sh

COPY entrypoint.sh /entrypoint.sh
RUN chmod 0700 /entrypoint.sh

EXPOSE 1194/udp

ENTRYPOINT ["/entrypoint.sh"]
CMD openvpn --config /etc/openvpn/openvpn.conf
