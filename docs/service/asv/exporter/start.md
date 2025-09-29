---
sidebar_position: 10
---

# start
操作概述: 启动exporter服务

命令参数:
```bash
无
```

使用示例:
```bash
acli service asv exporter start
```

结果示例:
```bash
checking before start: getcmdpid return 1, get pids: :Start (supervisor --lock-file '/var/run/supervisor/exporter.suplock' --flag-file '*' --flag 011 -w '/sf/bin/exporter -f /sf/etc/datareport/exporter-api.yaml') OK! 59981.
```