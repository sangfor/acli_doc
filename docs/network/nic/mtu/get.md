---
sidebar_position: 1
---

# get

### 操作概述

查看网口mtu

### 命令参数

```bash
-n|--nic-name=string    必要参数，网口名称，示例：eth1
```

### 使用示例

```bash
acli network nic mtu get --nic-name eth0
```

### 结果示例

```bash
eth0
   mtu: 1500
```
