---
sidebar_position: 1
---

# ip

### 操作概述

查看主机网络信息，支持只读查询地址、路由、链路及邻居信息

### 命令参数

```bash
addr show   查看主机地址信息（也可使用别名 a）
route show  查看路由信息
link show   查看链路信息
neigh show  查看邻居信息
```

### 使用示例

```bash
acli system ip route show
```

### 结果示例

```bash
default via 10.131.136.1 dev eth0
10.131.136.0/24 dev eth0 proto kernel scope link src 10.131.136.168
172.18.0.0/16 dev docker0 proto kernel scope link src 172.18.0.1
```
