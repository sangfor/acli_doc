---
sidebar_position: 1
---

# restart

### 操作概述

重启vtplogd服务

### 命令参数

无参数

### 使用示例

```bash
acli service asv vtplogd restart
```

### 结果示例
```bash
acli service asv vtplogd restart

Stoping vtplogd: :checking stop status: getcmdpid return 0, get pids: 223957 223969 4134515: .checking stop status: getcmdpid return 0, get pids: 223957 223969 4134515: .checking stop status: getcmdpid return 0, get pids: 223957 223969 4134515: .checking stop status: getcmdpid return 0, get pids: 223957: .checking stop status: getcmdpid return 0, get pids: 223957: .checking stop status: getcmdpid return 1, get pids: :  OK!.
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Start (/sf/bin/vtplogd &) OK!.
```
