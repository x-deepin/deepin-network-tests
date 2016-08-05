**描述**: dde-daemon 网络后端自动化测试工具集合

主要用于测试 deepin 网络后端基本功能是否异常，包括测试有线连接，无线连
接，pppoe 及 vpn 等。

由于测试网络功能需要搭建配套的服务，同时同一类型服务为测试不同的参数可
能需要配置多次，为方便部署，配合 Ansible 和 Docker 进行管理以方便自动
化测试。 另外部分网络功能如无线连接、802.1X企业级加密、PPPoE 无法通过
虚拟机、Docker 等容器技术进行测试，还需要 OpenWRT 路由器和额外的主机进
行配合，具体情况详见下面的使用说明。

## 依赖

- ansible
- [dde-daemon](https://github.com/linuxdeepin/dde-daemon)
- network-manager
- python2
- python2-docker>=1.7.0

## 使用说明

**准备阶段**
```
# systemctl enable docker.socket
# systemctl start docker.socket
```

TODO
- wired
- wired-static-ip
- wired-802.1x
- wireless
- wireless-static-ip
- wireless-802.1x
- pppoe
- vpn-l2tp
- vpn-strongswan
- vpn-pptp
- vpn-pptp-use-mppe
- vpn-openvpn
- vpn-openvpn-peap
- vpn-openvpn-ttls
- vpn-openconnect
- vpn-vpnc

## License

GNU General Public License Version 3
