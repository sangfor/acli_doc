---
sidebar_position: 1
---

# restart

### Overview

Restart redis service

### Command Parameters

No parameters

### Usage Example

```bash
acli service asv redis restart
```

### Output Example
```bash
acli service asv redis restart

Stoping redis-server: :checking stop status: getcmdpid return 1, get pids: :  OK!.
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Start (supervisor --lock-file '/var/run/supervisor/redis-server.suplock' --flag-file '*' --flag 011 -w '/sf/bin/redis-server /etc/redis/6379.conf') OK! 4125164.
```