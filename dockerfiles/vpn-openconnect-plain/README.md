**描述**: OpenConnect VPN Dockerfile 配置文件, 认证方式 plain

部署

```
# docker build --tag vpn-openconnect-plain .
```

运行

```
# docker run --detach --net host --privileged --publish-all vpn-openconnect-plain
```

帐户信息

```
认证方式: plain (需要弹出 openconnect auth 对话框输入用户名密码)
CA 证书: ./etc/ocserv/ca.crt
用户名: test
密码: test
```

证书生成方法

1. 安装 gnutls
2. 生成 CA 证书
   ```
   $ cd ./etc/ocserv/
   $ certtool --generate-privkey --outfile ca.key
   $ cat << _EOF_ >ca.tmpl
   cn = "VPN CA"
   organization = "Deepin QA Team"
   serial = 1
   expiration_days = -1
   ca
   signing_key
   cert_signing_key
   crl_signing_key
   _EOF_
   $ certtool --generate-self-signed --load-privkey ca.key --template ca.tmpl --outfile ca.crt
   ```
3. 生成服务端证书
   ```
   $ certtool --generate-privkey --outfile server.key
   $ cat << _EOF_ >server.tmpl
   cn = "VPN server"
   organization = "Deepin QA Team"
   expiration_days = -1
   signing_key
   encryption_key #only if the generated key is an RSA one
   tls_www_server
   # ip_address = "192.168.1.100"
   _EOF_
   $ certtool --generate-certificate --load-privkey server.key --load-ca-certificate ca.crt --load-ca-privkey ca.key --template server.tmpl --outfile server.crt
   ```
4. 配置用户名密码
   ```
   $ ocpasswd -c ./etc/ocservocpasswd test
   ```
