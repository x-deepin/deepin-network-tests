**描述**: OpenVPN Dockerfile 配置文件, 认证方式 TLS

部署

```
# docker build --tag vpn-openvpn-tls .
```

运行

```
# docker run --detach --net host --privileged --publish-all --name running-vpn-openvpn-tls vpn-openvpn-tls
```

停止

```
# docker stop running-vpn-openvpn-tls
# docker rm -f running-vpn-openvpn-tls
```

帐户信息

```
认证方式: TLS
CA证书: ./etc/openvpn/easy-rsa/pki/ca.crt
客户端证书: ./etc/openvpn/easy-rsa/pki/issued/client.crt
客户端密钥: ./etc/openvpn/easy-rsa/pki/private/client.key
客户端密码: test
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
