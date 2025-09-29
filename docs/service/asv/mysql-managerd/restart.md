---
sidebar_position: 10
---

# restart
操作概述: 重启mysql-managerd服务

命令参数:
```bash
无
```

使用示例:
```bash
acli service asv mysql-managerd restart
```

结果示例:
```bash
Stoping mysql-managerd: :  OK!.
Start (supervisor --lock-file '/var/run/supervisor/mysql-managerd.suplock' --flag-file '*' --flag 011 -w '/sf/cluster/bin/mysql-managerd -f /sf/etc/mysql-managerd/mysql-managerd.yaml') OK! 81990.
```