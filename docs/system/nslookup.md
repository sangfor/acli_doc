---
sidebar_position: 1
---

# nslookup

### 操作概述

执行 DNS 查询，获取域名或 IP 的解析记录（只读）。

### 命令参数

无参数

### 使用示例

```bash
acli system nslookup example.com
```

### 结果示例

```bash
# acli system nslookup example.com
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
Name:   example.com
Address: 93.184.216.34
```
