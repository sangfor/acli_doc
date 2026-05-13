---
sidebar_position: 1
---

# start

### 操作概述

启动vtpperlproxy服务

### 命令参数

无参数

### 使用示例

```bash
acli service asv vtpperlproxy start
```

### 结果示例
```bash
acli service asv vtpperlproxy start

 Physical cores < 16: 8checking before start: getcmdpid return 0, get pids: 4135746 4135749:checking before start: getcmdpid2 return 1, get pids: :Start (supervisor --flag-file '/var/run/vtpperlproxy.pid' --flag 010 -p '/sf/bin/vtpperlproxy,*vtpperlproxy' '/sf/bin/vtpperlproxy') OK!.
```
