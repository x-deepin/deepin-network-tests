**描述**: strongSwan/IKEv2 VPN Dockerfile 配置文件, 同时支持 EAP/Private Key(TLS) 两种认证方式

部署

```
# docker build --tag vpn-strongswan .
```

运行

```
# docker run --detach --net host --privileged --publish-all --env IPADDRESS=192.168.1.100 vpn-strongswan
```

帐户信息

```
认证方式: EAP
CA证书: ./etc/ipsec.d/cacerts/ca.crt
用户名: test
密码: test

认证方式: Private Key
CA证书: ./etc/ipsec.d/cacerts/ca.crt
客户端证书: ./etc/ipsec.d/certs/client.crt
客户端密钥: ./etc/ipsec.d/private/client.key
```

RSA 证书生成方法

1. 安装 strongswan
2. 生成 CA 证书
   ```
   $ cd ./etc/ipsec.d/
   $ ipsec pki --gen --type rsa --size 4096 --outform pem > private/ca.key
   $ ipsec pki --self --ca --lifetime 3650 --in private/ca.key --type rsa --dn "C=CH, O=strongSwan, CN=deepin qa team" --outform pem > cacerts/ca.crt
   ```
4. 生成服务端证书, 特别注意, 因为安全相关的原因, --san 后跟的
   subjectAltName 必须与服务器主机的 IP 地址相同, 否则无法连接成功, 所
   有为了避免这种问题, entrypoint.sh 会在每次启动 Docker 前服务根据传
   递的 $IPADDRESS 动态生成一份新的 certs/server.crt

   ```
   $ openssl req -newkey rsa:2048 -nodes -days 3650 -keyout private/server.key -out certs/server.crt
   $ ipsec pki --gen --type rsa --size 2048 --outform pem > private/server.key
   $ ipsec pki --pub --in private/server.key --type rsa | ipsec pki --issue --lifetime 3650 --cacert cacerts/ca.crt --cakey private/ca.key --dn "C=CH, O=strongSwan, CN=server cert" --san 192.168.1.100 --flag serverAuth --flag ikeIntermediate --outform pem > certs/server.crt
   ```
4. 生成客户端证书
   ```
   $ ipsec pki --gen --type rsa --size 2048 --outform pem > private/client.key
   $ ipsec pki --pub --in private/client.key --type rsa | ipsec pki --issue --lifetime 3650 --cacert cacerts/ca.crt --cakey private/ca.key --dn "C=CH, O=strongSwan, CN=client cert" --san 0.0.0.0 --outform pem > certs/client.crt
   ```
