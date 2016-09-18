**描述**: L2TP VPN Dockerfile 配置文件

部署

```
# docker build --tag vpn-l2tp .
```

运行

```
# docker run --detach --net host --privileged --publish-all --name running-vpn-l2tp vpn-l2tp
```

停止

```
# docker stop running-vpn-l2tp
# docker rm -f running-vpn-l2tp
```

帐户信息

```
用户名: test
密码: test
```
