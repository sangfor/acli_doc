---
sidebar_position: 1
---

# restart

### 操作概述

重启vtpperlproxy服务

### 命令参数

无参数

### 使用示例

```bash
acli service asv vtpperlproxy restart
```

### 结果示例
```bash
acli service asv vtpperlproxy restart

Stoping vtpperlproxy: :checking stop status: getcmdpid return 0, get pids: 136432 140773: .checking stop status: getcmdpid return 0, get pids: 136432 140773: .checking stop status: getcmdpid return 0, get pids: 136432 140773: .checking stop status: getcmdpid return 0, get pids: 136432 140773: .checking stop status: getcmdpid return 0, get pids: 136432 140773: .checking stop status: getcmdpid return 0, get pids: 136432 140773: .checking stop status: getcmdpid return 0, get pids: 136432 140773: .checking stop status: getcmdpid return 0, get pids: 136432 140773: .checking stop status: getcmdpid return 0, get pids: 136432 140773: .checking stop status: getcmdpid return 0, get pids: 136432 140773: . failed!
 -TERM time out, trying -KILL: :  OK!.
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Start (supervisor --flag-file '/var/run/vtpperlproxy.pid' --flag 010 -p '/sf/bin/vtpperlproxy,*vtpperlproxy' '/sf/bin/vtpperlproxy') OK!.
```
