**描述**: dde-daemon 网络后端自动化测试工具集合

主要用于测试 deepin 网络后端基本功能是否异常，包括测试有线连接，无线连
接，PPPoE 及 VPN 等。

由于测试网络功能需要搭建配套的服务，同时同一类型服务为测试不同的参数可
能需要配置多次，为方便部署，配合 Ansible 和 Docker 进行管理以方便自动
化测试。另外部分网络功能如无线连接、802.1X 企业级加密、PPPoE 无法通过虚
拟机、Docker 等容器技术进行测试，还需要 OpenWRT 路由器（router）和额外
的主机（server）进行配合，具体情况详见下面的使用说明。

## 依赖

**测试机**
- ansible
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

1. 修复 ssh 密钥权限

   执行 git clone 操作后, keys/id_rsa 文件权限会丢失, 应首先执行下面的
   操作进行修复, 否则 Ansible 无法正常使用
   ```
   $ make prepare-fix-keys-perm
   ```

1. 配置 hosts 文件

   编辑 hosts.example，将 server 和 router 对应的地址补充完整，然后保
   存为 hosts 文件

   ```
   $ cp hosts.example hosts
   ```

1. 配置路由器 SSH（可选，如果没有 OpenWRT 路由器可以跳过，执行测试时会忽略
   相关的测试用例）

   通过浏览器进入路由器，进入 System->Administration 页面，首先设置
   Router Password，否则无法通过 ssh 登录路由器，然后将公钥文件
   （./keys/id_rsa.pub）的内容复制到 SSH-Keys 下面的文本框，然后单击
   Save&Apply 进行保存。设置成功后，执行下面的命令可以不需要密码直接登
   录路由器：

   ```
   $ ssh -o 'IdentityFile="./keys/id_rsa"' root@192.168.1.1
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

   启用 root 用户

   ```
   # password root
   ```

   在测试机运行下面的命令将公钥添加到服务器

   ```
   $ make prepare_ssh
   ```

   以上步骤配置成功后，执行下面的命令可以不需要密码直接登录服务器：

   ```
   $ ssh -o 'IdentityFile="./keys/id_rsa"' root@192.168.1.xxx
   ```

1. 安装依赖

   **测试机**

   ```
   # apt-get install ansible
   ```

   **服务器**

   ```
   # apt-get install docker.io python2-docker
   ```

   因为 Ansible 依赖 python2，如果缺少相应包，可以通过 pip2 来安装

   ```
   # pip2 install 'docker-py>=1.7.0'
   ```

   **路由器**

   ```
   # opkg update
   # opkg install openssh-sftp-server python wpad
   ```

1. 部署 PPPoE、VPN、FreeRadius 等网络服务到服务器

   ```
   $ make deploy_services
   ```

## TODO 运行自动化测试

```
$ make test
```

## TODO 手动测试

帐号信息, 网络拓扑结构等具体可参考 dockerfiles 目录下对应的README, 比如 PPPoE

## 测试主机分布特别说明

测试无线网络功能时需要搭建 OpenWRT 路由器，测试 802.1X 企业级加密和 PPPoE
功能则还需要额外的服务器主机配合，此外的情况比如测试 VPN 则只需要测试
机单机也可完成测试，这种情况下网络服务要部署到测试机上，对应上面的配置
则是把 hosts server 地址改为 `127.0.0.1`，执行 make 命令时添加
`ANSIBLE_LOCAL=1` 选项，如

```
$ make deploy_services ANSIBLE_LOCAL=1
$ make test ANSIBLE_LOCAL=1
```

## TODO 测试用例集合

```
$ make debug_list_services
```

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
