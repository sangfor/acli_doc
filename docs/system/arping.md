---
sidebar_position: 1
---

# arping

### 操作概述

向指定主机发送 ARP 请求以探测其在线状态

### 命令参数

```bash
-c|--count=integer     指定发送的请求次数，示例：5
-i|--interface=string  指定使用的网卡接口，示例：eth0
-s|--source=string     指定源 IP 地址
<ip>                   必要参数，指定要探测的目标 IP，示例：10.10.1.2
```

### 使用示例

```bash
acli system arping -i eth0 -c 5 10.10.1.2
```

### 结果示例

```bash
ARPING 10.10.1.2 from 10.131.136.168 eth0
Unicast reply from 10.10.1.2 [00:0C:29:56:B7:A6]  1.342ms
Unicast reply from 10.10.1.2 [00:0C:29:56:B7:A6]  1.101ms
Unicast reply from 10.10.1.2 [00:0C:29:56:B7:A6]  1.252ms
Sent 3 probes (1 broadcast(s))
Received 3 response(s)
```
