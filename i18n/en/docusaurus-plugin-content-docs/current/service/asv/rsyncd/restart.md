---
sidebar_position: 1
---

# restart

### Overview

Restart rsyncd service

### Command Parameters

No parameters

### Usage Example

```bash
acli service asv rsyncd restart
```

### Output Example
```bash
acli service asv rsyncd restart

Stoping rsyncd: :checking stop status: getcmdpid return 0, get pids: 183919: .checking stop status: getcmdpid return 1, get pids: :  OK!.
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Start (supervisor --lock-file '/var/run/supervisor/rsyncd.suplock' --flag-file '*' --flag 011 -w '/usr/bin/rsyncd --daemon --no-detach --config=/sf/etc/rsyncd.conf --port=4151') OK! 4126757.
```