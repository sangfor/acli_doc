---
sidebar_position: 10
---

# start
操作概述: 启动mgmt-node-agent-api服务

命令参数:
```bash
无
```

使用示例:
```bash
acli service asv mgmt-node-agent-api start
```

结果示例:
```bash
Physical cores < 16: 8checking before start: getcmdpid return 0, get pids: 903065 903069:checking before start: getcmdpid2 return 1, get pids: :Start (supervisor --lock-file '/var/run/supervisor/mgmt-node-agent-api.suplock' --flag-file '*' --flag 011 -w '/sf/bin/mgmt-node-agent-api --config-file /sf/etc/mgmt-node-agent/mgmt-node-agent-api.conf') OK!.
```