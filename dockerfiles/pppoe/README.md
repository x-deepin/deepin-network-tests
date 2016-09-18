**描述**: PPPoE Dockerfile 配置文件

部署

```
# docker build --tag pppoe .
```

运行

**注意需要传递环境变量 INTERFACE，即主机对应的有线设备接口**

```
# docker run --detach --net host --privileged --publish-all --env INTERFACE=eth0 --name running-pppoe pppoe
```

停止

```
# docker stop running-pppoe
# docker rm -f running-pppoe
```

帐户信息

```
ISP服务商: isp
用户名: test
密码: test
```
