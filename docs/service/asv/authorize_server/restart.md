---
sidebar_position: 1
---

# restart

### 操作概述

重启authorize_server服务

### 命令参数

无参数

### 使用示例

```bash
acli service asv authorize_server restart
```

### 结果示例
```bash
acli service asv authorize_server restart

Already stoped: authorize_server
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Start (supervisor --flag-file '/var/run/authorize_server.pid' --flag 010 -w '/sf/sgp/license/bin/sf_license_env /sf/authorize/bin/authorize_server -l 6') OK! 4106229.
```
