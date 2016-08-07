**描述**: PPTP VPN Dockerfile 配置文件, 关闭 MPPE 选项

部署

```
# docker build --tag vpn-pptp-no-mppe .
```

运行

```
# docker run --detach --net host --privileged --publish 1723:1723 vpn-pptp
```

帐户信息

```
用户名: test
密码: test
```
