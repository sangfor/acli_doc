---
sidebar_position: 1
---

# start

### 操作概述

启动vtpdaemon服务

### 命令参数

无参数

### 使用示例

```bash
acli service asv vtpdaemon start
```

### 结果示例
```bash
acli service asv vtpdaemon start

 Physical cores < 16: 8checking before start: getcmdpid return 0, get pids: 4130670 4130715 4130720 4131165 4132427 4133450 4133945:checking before start: getcmdpid2 return 0, get pids: 4133945 4133450 4132427 4131165 4130720 4130715:[is_supervisor_running] supervisor exits.:Already runing: vtpdaemon 4130715 ... (warning).
```
