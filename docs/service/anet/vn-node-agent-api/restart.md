---
sidebar_position: 10
---

# restart
操作概述: 重启vn-node-agent-api服务

命令参数:
```bash
无
```

使用示例:
```bash
acli service anet vn-node-agent-api restart
```

结果示例:
```bash
Stoping vn-node-agent-api: : .  OK!.
Start (supervisor --flag-file '/var/run/vn-node-agent-api.pid' --flag 010 -p '/sf/vn/bin/vn-node-agent-api --config-file /sf/vn/etc/vn-node-agent/vn-node-agent-api.conf',*vn-node-agent-api*) OK!.
```