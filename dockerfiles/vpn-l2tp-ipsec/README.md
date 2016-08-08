**描述**: L2TP VPN Dockerfile 配置文件, 启用 IPSec/strongSwan 支持

部署

```
# docker build --tag vpn-l2tp-ipsec .
```

运行

```
# docker run --detach --net host --privileged --publish-all vpn-l2tp-ipsec
```

帐户信息

```
用户名: test
密码: test
IPSec Pre-Shared Key: test
```
