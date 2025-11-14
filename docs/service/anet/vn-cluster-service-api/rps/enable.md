---
sidebar_position: 10
---

# enable
操作概述: 启用负载均衡RPS

命令参数:
```bash
--hosts=string     必要参数：主机id列表，多个id之间使用逗号分隔，例如：host-002987263c8g,host-761846915f3m
```

使用示例:
```bash
acli service anet vn-cluster-service-api rps enable --hosts host-002987263c8g,host-761846915f3m
```

结果示例:
```bash
task_id: host-005056b2ec8d:00009AFB:1ADD4A0:6874A955
```