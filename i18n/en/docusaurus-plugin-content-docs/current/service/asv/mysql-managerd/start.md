---
sidebar_position: 1
---

# start

### Overview

Start the mysql-managerd service

### Command Parameters

No parameters

### Usage Example

```bash
acli service asv mysql-managerd start
```

### Output Example

```bash
Start (supervisor --lock-file '/var/run/supervisor/mysql-managerd.suplock' --flag-file '*' --flag 011 -w '/sf/cluster/bin/mysql-managerd -f /sf/etc/mysql-managerd/mysql-managerd.yaml') OK! 78871.
```