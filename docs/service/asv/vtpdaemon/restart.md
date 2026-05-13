---
sidebar_position: 1
---

# restart

### 操作概述

重启vtpdaemon服务

### 命令参数

无参数

### 使用示例

```bash
acli service asv vtpdaemon restart
```

### 结果示例
```bash
acli service asv vtpdaemon restart

Stoping vtpdaemon: :checking stop status: getcmdpid return 1, get pids: :  OK!.
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Start (supervisor --flag-file '/var/run/vtpdaemon.pid' --flag 010 -p '/sf/bin/vtpdaemon,*vtpdaemon' '/sf/bin/vtpdaemon') OK!.
```
