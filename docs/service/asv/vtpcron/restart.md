---
sidebar_position: 1
---

# restart

### 操作概述

重启vtpcron服务

### 命令参数

无参数

### 使用示例

```bash
acli service asv vtpcron restart
```

### 结果示例
```bash
acli service asv vtpcron restart

Stoping vtpcron: :checking stop status: getcmdpid return 0, get pids: 229170 229188: .checking stop status: getcmdpid return 0, get pids: 229170 229188: .checking stop status: getcmdpid return 0, get pids: 229170 229188: .checking stop status: getcmdpid return 1, get pids: :  OK!.
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Start (/sf/bin/vtpcron) OK!.
```
