# References:
#   https://github.com/TommyLau/docker-ocserv
#   https://www.vultr.com/docs/setup-openconnect-vpn-server-for-cisco-anyconnect-on-ubuntu-14-04-x64
#   https://www.logcg.com/archives/1343.html
#   https://github.com/wppurking/ocserv-docker

FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y iptables ocserv gnutls-bin

COPY ./etc/ocserv/ /etc/ocserv/

COPY entrypoint.sh /entrypoint.sh
RUN chmod 0700 /entrypoint.sh

EXPOSE 443/tcp 443/udp

ENTRYPOINT ["/entrypoint.sh"]
CMD ocserv --debug 999 --foreground
