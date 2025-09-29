---
sidebar_position: 10
---

# stop
操作概述: 停止vtpstatd服务

命令参数:
```bash
无
```

使用示例:
```bash
acli service asv vtpstatd stop
```

结果示例:
```bash
Stoping vtpstatd: :checking stop status: getcmdpid return 0, get pids: 38798 38799 38800 38806 38807: .checking stop status: getcmdpid return 0, get pids: 38798 38799 38800 38806 38807: .checking stop status: getcmdpid return 0, get pids: 38798 38800 38806 38807: .checking stop status: getcmdpid return 0, get pids: 38798 38800 38806 38807: .checking stop status: getcmdpid return 0, get pids: 38798 38800 38806 38807: .checking stop status: getcmdpid return 0, get pids: 38798 38800 38806 38807: .checking stop status: getcmdpid return 0, get pids: 38798 38800 38806 38807: .checking stop status: getcmdpid return 0, get pids: 38798 38800 38806 38807: .checking stop status: getcmdpid return 0, get pids: 38798 38800 38806: .checking stop status: getcmdpid return 0, get pids: 38798 38800 38806: . failed!
 -TERM time out, trying -KILL: : .  OK!.
```