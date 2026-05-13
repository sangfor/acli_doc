---
sidebar_position: 1
---

# restart

### 操作概述

重启pmxcfs服务

### 命令参数

无参数

### 使用示例

```bash
acli service asv pmxcfs restart
```

### 结果示例
```bash
acli service asv pmxcfs restart

Stoping pmxcfs: :checking stop status: getcmdpid return 0, get pids: 52468: .checking stop status: getcmdpid return 0, get pids: 52468: .checking stop status: getcmdpid return 0, get pids: 52468: .checking stop status: getcmdpid return 1, get pids: :  OK!.
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Start (/sf/cluster/bin/pmxcfs -f -w &) OK! 4124167.
```
