---
sidebar_position: 1
---

# restart

### 操作概述

重启corosync服务

### 命令参数

无参数

### 使用示例

```bash
acli service asv corosync restart
```

### 结果示例
```bash
acli service asv corosync restart

Stoping corosync: :checking stop status: getcmdpid return 1, get pids: :  OK!.
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Start (supervisor --flag-file '/var/run/corosync.pid' --flag 010 --test-interval 1 --prerun '/sf/cluster/bin/precorosync.sh' -w '/sf/cluster/sbin/corosync -f') OK!.
```
