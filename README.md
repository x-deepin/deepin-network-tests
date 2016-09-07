**描述**: deepin 网络模块自动化测试

配合 ansbile/docker/openwrt 等技术，实现 deepin 网络功能自动化测试，以确保上游升级网络组件时相关功能正常。目前已经涵盖的内容包括：

- pppoe
- vpn-l2tp (l2tp/ipsec)
- vpn-openconnect (cert/plain)
- vpn-openvpn (password/tls)
- vpn-pptp (mppe/no-mppe)
- vpn-strongswan (privatekey/eap)
- wireless-wep
- wireless-wpa-psk
- wireless-wpa-eap (tls/ttls/peap)

## 依赖

**测试机**
- ansible>=2.1.0
- [dde-daemon](https://github.com/linuxdeepin/dde-daemon)
- network-manager
- python2

**服务器**
- docker.io
- python2-docker>=1.7.0

**OpenWRT 路由器**
- OpenWRT>=15.05.1(CHAOS CALMER)
- openssh-sftp-server
- python
- wpad

## 准备阶段

1. 配置 hosts 文件

   编辑 hosts.example，将 server 和 router 对应的地址补充完整，然后保
   存为 hosts 文件

   ```
   $ cp hosts.example hosts
   ```

1. 修复 SSH 密钥权限

   执行 git clone 操作后, keys/id_rsa 文件权限会丢失, 应首先执行下面的
   操作进行修复, 否则 Ansible 无法正常使用
   ```
   $ make prepare-fix-keys-perm
   ```

1. 配置路由器 SSH（可选，如果没有 OpenWRT 路由器可以跳过，执行测试时会忽略
   相关的测试用例）

   通过浏览器进入路由器，进入 System->Administration 页面，首先设置
   Router Password，否则无法通过 ssh 登录路由器，然后将公钥文件
   （./keys/id_rsa.pub）的内容复制到 SSH-Keys 下面的文本框，然后单击
   Save&Apply 进行保存。设置成功后，执行下面的命令可以不需要密码直接登
   录路由器：

   ```
   $ ssh -o 'IdentityFile="./ansible/keys/id_rsa"' root@192.168.1.1
   ```

1. 配置服务器 SSH

   配置 ssh 服务端，编辑 /etc/ssh/sshd_config 打开选项
   'PermitRootLogin yes'，后开启 ssh、docker 服务

   ```
   # systemctl enable ssh.socket
   # systemctl start ssh.socket
   # systemctl enable docker.socket
   # systemctl start docker.socket
   ```

   启用 root 用户，即为 root 用户设置密码

   ```
   # passwd root
   ```

   在测试机运行下面的命令将公钥添加到服务器，会提示输入服务机的 root
   密码

   ```
   $ make prepare-ssh
   ```

   以上步骤配置成功后，执行下面的命令可以不需要密码直接登录服务器：

   ```
   $ ssh -o 'IdentityFile="./ansible/keys/id_rsa"' root@192.168.1.xxx
   ```

1. 安装依赖

   **测试机**

   ```
   # apt-get install docker.io python-docker
   # apt-get install ansible network-manager-strongswan
   ```

   **服务器**

   ```
   # apt-get install docker.io python-docker
   ```

   因为 Ansible 依赖 python2，如果缺少相应包，也可以通过 pip2 来安装

   ```
   # pip2 install 'docker-py>=1.7.0'
   ```

   **路由器**

   ```
   # opkg update
   # opkg install openssh-sftp-server python
   # opkg install --force-depends wpad
   ```

1. 部署 PPPoE、VPN、FreeRadius 等网络服务到服务器

   **方法一：**
   推荐直接从hub.deepin.io docker仓库pull：
   ```
   $ docker pull hub.deepin.io/ubuntu:16.10
   $ docker pull hub.deepin.io/ubuntu/freeradius:latest
   $ docker pull hub.deepin.io/ubuntu/pppoe:latest
   $ docker pull hub.deepin.io/ubuntu/vpn-l2tp-ipsec:latest
   $ docker pull hub.deepin.io/ubuntu/vpn-l2tp:latest
   $ docker pull hub.deepin.io/ubuntu/vpn-openconnect-cert:latest
   $ docker pull hub.deepin.io/ubuntu/vpn-openconnect-plain:latest
   $ docker pull hub.deepin.io/ubuntu/vpn-openvpn-password:latest
   $ docker pull hub.deepin.io/ubuntu/vpn-openvpn-tls:latest
   $ docker pull hub.deepin.io/ubuntu/vpn-pptp:latest
   $ docker pull hub.deepin.io/ubuntu/vpn-pptp-no-mppe:latest
   $ docker pull hub.deepin.io/ubuntu/vpn-strongswan:latest
   ```

   **方法二：**
   ```
   $ make deploy-services
   ```

   如果部署失败, 有可能是获取 Docker 镜像 ubuntu:16.10 失败, 可以先到服
   务器手动更新
   ```
   # docker pull ubuntu:16.10
   ```

   另外也可以单独部署指定服务, 如
   ```
   $ make deploy-service-openvpn-password
   ```

   当前支持的服务列表可以通过下面的命令获取
   ```
   $ make list-services
   ```

## 运行自动化测试

执行所有测试
```
$ make run-tests
```

执行单个测试
```
$ cd tests
$ ./test_network_xxx.py
$ python3 -m unittest test_network_xxx.TestClaass.test_method
```

## 手动测试（用于辅助 QA 人员测试网络功能）

手动测试时，可以跳过准备阶段中配置 SSH 相关的步骤，例如要测试 vpn-pptp，
找一台机器作为服务器，运行下面的命令启动 PPTP 服务
```
$ make deploy-service-vpn-pptp ANSIBLE_LOCAL=1
$ make start-service-vpn-pptp ANSIBLE_LOCAL=1
```

然后到测试机手动创建 VPN 连接进行测试，测试过程中用到的帐号等信息可参
考 dockerfiles 目录下对应的 README 文档。

测试完成后到服务器关闭 PPTP 服务
```
$ make stop-service-vpn-pptp ANSIBLE_LOCAL=1
```

## 安全风险

为实现公司 lava 自动化测试，目前 SSH 密钥也在 git 版本控制下，为降低安
全风险，需要涉及的的主机不连接外网或不要将该项目同步到外部。

## License

GNU General Public License Version 3
