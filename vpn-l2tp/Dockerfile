# Run: /usr/bin/start-service
# References:
#   http://www.debian-tutorials.com/install-and-configure-pppoe-server-on-debian-squeeze
#   http://www.howtodoityourself.org/pppoe-server-how-to-do-it-yourself.html

FROM debian:sid

#TODO: 
# change source server
# RUN echo 'Server = http://mirror.bjtu.edu.cn/archlinux/$repo/os/$arch' > /etc/pacman.d/mirrorlist

# install packages
RUN apt-get update
RUN apt-get install rp-pppoe

# configuration
RUN echo 'require-chap'          > /etc/ppp/pppoe-server-options; \
    echo 'login'                 >> /etc/ppp/pppoe-server-options; \
    echo 'lcp-echo-interval 10'  >> /etc/ppp/pppoe-server-options; \
    echo 'lcp-echo-failure 2'    >> /etc/ppp/pppoe-server-options; \
    echo 'ms-dns 8.8.8.8'        >> /etc/ppp/pppoe-server-options; \
    echo 'ms-dns 8.8.4.4'        >> /etc/ppp/pppoe-server-options; \
    echo 'netmask 255.255.255.0' >> /etc/ppp/pppoe-server-options; \
    echo 'defaultroute'          >> /etc/ppp/pppoe-server-options; \
    echo 'noipdefault'           >> /etc/ppp/pppoe-server-options; \
    echo 'usepeerdns'            >> /etc/ppp/pppoe-server-options; \
    echo '"test"          *        "test"         *' > /etc/ppp/chap-secrets; \
    echo '192.168.72.100-200' > /etc/ppp/allip

# runner script
RUN echo '#!/bin/sh' > /usr/bin/start-service; \
    echo '/usr/bin/pppoe-server -C isp -L 192.168.72.1 -p /etc/ppp/allip -I eth0' >> /usr/bin/start-service; \
    chmod +x /usr/bin/start-service

# sysctl net.ipv4.ip_forward=1
# iptables -A POSTROUTING -t nat -s 10.211.55.0/24 -j MASQUERADE  
 
# define default command
CMD ["/usr/bin/start-service"]
