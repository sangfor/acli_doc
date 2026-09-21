---
sidebar_position: 1
---

# traceroute

### 操作概述

追踪数据包到达目标主机的网络路径（只读）。

### 命令参数

无参数

### 使用示例

```bash
acli system traceroute -n 8.8.8.8
```

### 结果示例

```bash
# acli system traceroute -n 8.8.8.8
traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets
 1  10.0.0.1  0.324 ms  0.289 ms  0.312 ms
 2  192.168.1.1  1.025 ms  0.998 ms  1.112 ms
 3  8.8.8.8  10.231 ms  10.198 ms  10.245 ms
```
