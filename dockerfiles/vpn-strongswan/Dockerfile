# References:
#   https://wiki.strongswan.org/projects/strongswan/wiki/NetworkManager
#   https://www.strongswan.org/docs/LinuxKongress2009-strongswan.pdf
#   https://www.zeitgeist.se/2013/11/22/strongswan-howto-create-your-own-vpn/
#   https://raymii.org/s/tutorials/IPSEC_vpn_with_Ubuntu_15.04.html

FROM ubuntu:16.10

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y iptables strongswan libcharon-extra-plugins

COPY ./etc/ipsec.conf /etc/ipsec.conf
COPY ./etc/ipsec.secrets /etc/ipsec.secrets
COPY ./etc/ipsec.d/cacerts/ca.crt /etc/ipsec.d/cacerts/ca.crt
COPY ./etc/ipsec.d/private/ca.key /etc/ipsec.d/private/ca.key
COPY ./etc/ipsec.d/certs/server.crt /etc/ipsec.d/certs/server.crt
COPY ./etc/ipsec.d/private/server.key /etc/ipsec.d/private/server.key
COPY ./etc/ipsec.d/certs/client.crt /etc/ipsec.d/certs/client.crt
COPY ./etc/ipsec.d/private/client.key /etc/ipsec.d/private/client.key

COPY entrypoint.sh /entrypoint.sh
RUN chmod 0700 /entrypoint.sh

EXPOSE 500/udp 4500/udp

ENTRYPOINT ["/entrypoint.sh"]
CMD ipsec start --nofork
