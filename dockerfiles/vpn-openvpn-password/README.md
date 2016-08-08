**描述**: OpenVPN Dockerfile 配置文件

部署

```
# docker build --tag vpn-openvpn-password .
```

运行

```
# docker run --detach --net host --privileged --publish-all vpn-openvpn-password
```

帐户信息

```
认证类型: password
用户名: test
密码: test
CA证书: ./etc/openvpn/easy-rsa/pki/ca.crt
```

RSA 证书生成方法

1. 安装 easy-rsa
2. 初始化 easy-rsa 配置环境
   ```
   $ cp -rf /etc/easy-rsa ./etc/openvpn/
   $ cd ./etc/openvpn/easy-rsa
   $ easyrsa init-pki
   ```
3. 生成 CA 证书
   ```
   $ easyrsa buld-ca nopass
   ```
4. 生成服务端证书
   ```
   $ easyrsa build-server-full server nopass
   ```
4. 生成客户端证书
   ```
   $ easyrsa build-client-full client
   ```
5. 生成 dh.pem (Diffie Hellman parameters)
   ```
   $ easyrsa gen-dh
   ```
