---
sidebar_position: 1
---

# dpping

### 操作概述

通过 SDN 数据面执行 ping，检查到目标地址的连通性。

### 命令参数

命令格式：

```bash
acli network dpping [-c count] [-i interval] [-w deadline] [-s packetsize] [-M hint] [hop1 ...] destination
```

以下参数对应工具帮助中列出的用法：

```text
destination       必要参数，目标地址
-c count          指定发送的探测报文数量
-i interval       指定发送探测报文的时间间隔
-w deadline       指定探测的截止时间
-s packetsize     指定探测报文大小
-M hint           指定路径 MTU 发现策略
[hop1 ...]        可选的中间跳点
```

### 使用示例

```bash
acli network dpping
```

### 结果示例

未指定目标地址时返回以下用法提示，其中 `ping` 为工具帮助中的名称：

```text
dp ping: support ping with sdn dataplane
Usage: ping [-c count] [-i interval] [-w deadline] [-s packetsize]
            [-M mtu discovery hint] [hop1 ...] destination
```
