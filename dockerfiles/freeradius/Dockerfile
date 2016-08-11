# References:
#   https://github.com/ocedo/docker-freeradius
#   https://github.com/catatnight/docker-freeradius

FROM ubuntu:16.10

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y iptables freeradius

COPY ./etc/freeradius/ /etc/freeradius/

COPY entrypoint.sh /entrypoint.sh
RUN chmod 0700 /entrypoint.sh

EXPOSE 1812/tcp 1812/udp

ENTRYPOINT ["/entrypoint.sh"]
CMD freeradius -X
