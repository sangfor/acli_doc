---
sidebar_position: 1
---

# restart

### 操作概述

重启authorize_client服务

### 命令参数

无参数

### 使用示例

```bash
acli service asv authorize_client restart
```

### 结果示例
```bash
acli service asv authorize_client restart

Already stoped: authorize_client
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Start (supervisor --lock-file '/var/run/supervisor/authorize_client.suplock' --flag-file '*' --flag 011 -w '/sf/authorize/bin/authorize_client --config /sf/etc/authorize_client/authorize_client_config.json') OK!.
```
