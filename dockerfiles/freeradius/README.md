**描述**: FreeRadius Dockerfile 配置文件, 认证方式支持 EAP/TLS, EAP/PEAP, EAP/TTLS

部署

```
# docker build --tag freeradius .
```

运行

```
# docker run --detach --net host --privileged --publish-all --name running-freeradius freeradius
```

停止

```
# docker stop running-freeradius
# docker rm -f running-freeradius
```

帐户信息

```
路由器认证密码: routerpwd
客户端 Wireless 认证方式: WPA/WP2 Enterprise

EAP Auth: TLS
Identity: test
CA证书: ./etc/freeradius/certs/ca.pem
客户端证书: ./etc/freeradius/certs/client.pem
客户端密钥: ./etc/freeradius/certs/client.key
客户端密码: test

EAP Auth: TTLS
Identity: test
CA证书: ./etc/freeradius/certs/ca.pem
客户端密码: test

EAP Auth: PEAP
Identity: test
CA证书: ./etc/freeradius/certs/ca.pem
客户端密码: test
```

RSA 证书生成方法

1. 复制 freeradius 源码下的 certs 目录
   ```
   $ cp -rf ${freeradius_src}/raddb/certs ./etc/freeradius/certs/
   ```
2. 编辑 ca.cnf/server.cnf/client.cnf 设置默认证书密码
3. 生成测试用证书
   ```
   $ make destroycerts
   $ make
   ```
