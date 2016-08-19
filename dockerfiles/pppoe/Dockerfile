# References:
#   http://www.debian-tutorials.com/install-and-configure-pppoe-server-on-debian-squeeze
#   http://www.howtodoityourself.org/pppoe-server-how-to-do-it-yourself.html

FROM ubuntu:16.10

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y pppoe iptables

COPY ./etc/pppoe-ip-range /etc/pppoe-ip-range
COPY ./etc/ppp/pppoe-server-options /etc/ppp/pppoe-server-options
COPY ./etc/ppp/chap-secrets  /etc/ppp/chap-secrets
RUN chmod 0600 /etc/ppp/chap-secrets

COPY entrypoint.sh /entrypoint.sh
RUN chmod 0700 /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD pppoe-server -C isp -L 10.99.99.1 -p /etc/pppoe-ip-range -I ${INTERFACE} && while ps axg | grep -vw grep | grep -w pppoe-server > /dev/null; do sleep 1; done
