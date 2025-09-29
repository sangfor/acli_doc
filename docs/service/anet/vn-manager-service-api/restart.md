---
sidebar_position: 10
---

# restart
操作概述: 重启vn-manager-service-api服务

命令参数:
```bash
无
```

使用示例:
```bash
acli service anet vn-manager-service-api restart
```

结果示例:
```bash
Stoping vn-manager-service-api: : .  OK!.
Start (supervisor --flag-file '/var/run/vn-manager-service-api.pid' --flag 010 -p '/sf/vn/bin/vn-manager-service-api --config-file /sf/vn/etc/vn-manager-service/vn-manager-service-api.conf',*vn-manager-service-api*) OK!.
```