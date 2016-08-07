# References:
#   https://github.com/mobtitude/docker-vpn-pptp

FROM ubuntu:16.10

# NOTE: use pptpd=1.4.0-7 instead to avoid system bus access issue in pptpd.postinst if based on ubuntu:16.04
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y pptpd iptables

COPY ./etc/pptpd.conf        /etc/pptpd.conf
COPY ./etc/ppp/pptpd-options /etc/ppp/pptpd-options
COPY ./etc/ppp/chap-secrets  /etc/ppp/chap-secrets

COPY entrypoint.sh /entrypoint.sh
RUN chmod 0700 /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["pptpd", "--fg"]
