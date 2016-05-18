**描述**: dde-daemon 网络后端自动化测试工具集合

主要用于测试 deepin 网络后端基本功能是否异常，包括测试有线连接，无线连
接，pppoe 及 vpn 等。

由于部分网络功能如无线连接、802.1X企业级加密、PPPoE 无法通过虚拟机、
Docker 等容器技术进行测试，为增加部署的灵活性，工具分为服务端和客户端
两部分，服务端用于部署测试环境，例如通过 Docker 启动 VPN 服务，客户端
用于运行测试用例，两者通过 JSON-RPC 进行通信。

## 依赖

TODO
**server**
- python3
- python3-docker

python2-docker-py>=1.7.0

**client**
- python3
- [dde-daemon](https://github.com/linuxdeepin/dde-daemon)
- network-manager

## 使用说明

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
