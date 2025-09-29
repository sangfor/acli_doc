---
sidebar_position: 10
---

# restart
操作概述: 重启vtpstatd服务

命令参数:
```bash
无
```

使用示例:
```bash
acli service asv vtpstatd restart
```

结果示例:
```bash
Stoping vtpstatd: :checking stop status: getcmdpid return 0, get pids: 24896 24914 24957 24980 24996: .checking stop status: getcmdpid return 0, get pids: 24896 24914 24957 24980 24996: .checking stop status: getcmdpid return 0, get pids: 24896 24957 24980 24996: .checking stop status: getcmdpid return 0, get pids: 24896 24957 24980 24996: .checking stop status: getcmdpid return 0, get pids: 24896 24980 24996: .checking stop status: getcmdpid return 0, get pids: 24896 24980 24996: .checking stop status: getcmdpid return 0, get pids: 24896 24980: .checking stop status: getcmdpid return 0, get pids: 24896 24980: .checking stop status: getcmdpid return 0, get pids: 24896 24980: .checking stop status: getcmdpid return 0, get pids: 24896 24980: . failed!
 -TERM time out, trying -KILL: : .  OK!.
checking before start: getcmdpid return 1, get pids: :Start (/sf/bin/vtpstatd &) OK!.
```