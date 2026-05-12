---
sidebar_position: 1
---

# restart

### 操作概述

重启redis服务

### 命令参数

无参数

### 使用示例

```bash
acli service asv redis restart
```

### 结果示例
```bash
acli service asv redis restart

Stoping redis-server: :checking stop status: getcmdpid return 1, get pids: :  OK!.
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Start (supervisor --lock-file '/var/run/supervisor/redis-server.suplock' --flag-file '*' --flag 011 -w '/sf/bin/redis-server /etc/redis/6379.conf') OK! 4125164.
```
