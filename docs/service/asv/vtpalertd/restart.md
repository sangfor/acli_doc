---
sidebar_position: 1
---

# restart

### 操作概述

重启vtpalertd服务

### 命令参数

无参数

### 使用示例

```bash
acli service asv vtpalertd restart
```

### 结果示例
```bash
acli service asv vtpalertd restart

Stoping vtpalertd: :checking stop status: getcmdpid return 0, get pids: 163727 223897 223906 223919 223925 223927 223931 223942: .checking stop status: getcmdpid return 0, get pids: 163727 223897 223906 223919 223925 223927 223931 223942: .checking stop status: getcmdpid return 0, get pids: 163727 223897 223906 223919 223925 223927 223931 223942: .checking stop status: getcmdpid return 0, get pids: 163727 223897 223906 223919 223925 223927 223931 223942: .checking stop status: getcmdpid return 0, get pids: 163727 223897 223906 223919 223925 223927 223931 223942: .checking stop status: getcmdpid return 0, get pids: 163727 223897 223906 223925 223927 223931 223942: .checking stop status: getcmdpid return 0, get pids: 163727 223897 223906 223925 223927 223931 223942: .checking stop status: getcmdpid return 0, get pids: 163727 223897 223906 223925 223927 223931 223942: .checking stop status: getcmdpid return 0, get pids: 163727 223897 223906 223925 223927 223931 223942: .checking stop status: getcmdpid return 0, get pids: 163727 223906 223925 223927 223931 223942: . failed!
 -TERM time out, trying -KILL: : .  OK!.
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Start (/sf/bin/vtpalertd) OK! 4128681.
```
