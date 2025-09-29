---
sidebar_position: 10
---

# restart
操作概述: 重启exporter服务

命令参数:
```bash
无
```

使用示例:
```bash
acli service asv exporter restart
```

结果示例:
```bash
Stoping exporter: :checking stop status: getcmdpid return 1, get pids: :  OK!.
checking before start: getcmdpid return 1, get pids: :Start (supervisor --lock-file '/var/run/supervisor/exporter.suplock' --flag-file '*' --flag 011 -w '/sf/bin/exporter -f /sf/etc/datareport/exporter-api.yaml') OK! 61536.
```