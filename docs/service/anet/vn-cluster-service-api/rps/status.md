---
sidebar_position: 10
---

# status
操作概述: 获取主机负载均衡RPS的启用状态

命令参数:
```bash
无
```

使用示例:
```bash
acli service anet vn-cluster-service-api rps status
```

结果示例:
```bash
[0]
  hostId: host-002987263c8g
  isEnabled: 1
[1]
  hostId: host-761846915f3m
  isEnabled: 0
```