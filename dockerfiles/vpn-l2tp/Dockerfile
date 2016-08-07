# References:
#   https://github.com/hwdsl2/docker-ipsec-vpn-server
#   https://github.com/mcassiano/docker-l2tp-ipsec-vpn
#   https://github.com/philpl/docker-strongswan
#   https://help.ubuntu.com/community/L2TPServer
#   https://raymii.org/s/tutorials/IPSEC_L2TP_vpn_with_Ubuntu_14.04.html

FROM ubuntu:16.10

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y iptables xl2tpd

COPY ./etc/xl2tpd/xl2tpd.conf /etc/xl2tpd/xl2tpd.conf
COPY ./etc/ppp/options.xl2tpd /etc/ppp/options.xl2tpd
COPY ./etc/ppp/chap-secrets  /etc/ppp/chap-secrets

COPY entrypoint.sh /entrypoint.sh
RUN chmod 0700 /entrypoint.sh

EXPOSE 1701/udp

ENTRYPOINT ["/entrypoint.sh"]
CMD mkdir -p /var/run/xl2tpd && xl2tpd -D
