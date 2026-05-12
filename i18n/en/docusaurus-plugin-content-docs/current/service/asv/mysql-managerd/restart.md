---
sidebar_position: 1
---

# restart

### Overview

Restart the mysql-managerd service

### Command Parameters

No parameters

### Usage Example

```bash
acli service asv mysql-managerd restart
```

### Output Example

```bash
Stoping mysql-managerd: :  OK!.
Start (supervisor --lock-file '/var/run/supervisor/mysql-managerd.suplock' --flag-file '*' --flag 011 -w '/sf/cluster/bin/mysql-managerd -f /sf/etc/mysql-managerd/mysql-managerd.yaml') OK! 81990.
```