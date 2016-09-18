**描述**: PPTP VPN Dockerfile 配置文件

部署

```
# docker build --tag vpn-pptp .
```

运行

```
# docker run --detach --net host --privileged --publish-all --name running-vpn-pptp vpn-pptp
```

停止

```
# docker stop running-vpn-pptp
# docker rm -f running-vpn-pptp
```

帐户信息

```
用户名: test
密码: test
```
