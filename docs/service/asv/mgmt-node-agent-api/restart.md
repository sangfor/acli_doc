---
sidebar_position: 10
---

# restart
操作概述: 重启mgmt-node-agent-api服务

命令参数:
```bash
无
```

使用示例:
```bash
acli service asv mgmt-node-agent-api restart 
```

结果示例:
```bash
Stoping mgmt-node-agent-api: :checking stop status: getcmdpid return 1, get pids: :  OK!.
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Start (supervisor --lock-file '/var/run/supervisor/mgmt-node-agent-api.suplock' --flag-file '*' --flag 011 -w '/sf/bin/mgmt-node-agent-api --config-file /sf/etc/mgmt-node-agent/mgmt-node-agent-api.conf') OK!.
```