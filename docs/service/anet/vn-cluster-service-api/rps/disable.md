---
sidebar_position: 1
---

# disable

### 操作概述

启用主机负载均衡RPS

### 命令参数

```bash
-h|--hosts=array    必要参数，主机ID列表，例如：-h.1 host-005056894c2e -h.2 host-00505689413s
--hosts.N=string    hosts参数中的每个元素，示例：host-005056894c2e
```

### 使用示例

```bash
acli service anet vn-cluster-service-api rps disable -h.1 host-002987263c8g -h.2 host-761846915f3m
```

### 结果示例

```bash
taskId: host-005056b2ec8d:00009AFB:1ADD4A0:6874A955
```
