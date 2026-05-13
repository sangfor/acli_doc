---
sidebar_position: 1
---

# restart

### Overview

Restart the corosync service

### Command Parameters

No parameters

### Usage Example

```bash
acli service asv corosync restart
```

### Output Example
```bash
acli service asv corosync restart

Stoping corosync: :checking stop status: getcmdpid return 1, get pids: :  OK!.
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Start (supervisor --flag-file '/var/run/corosync.pid' --flag 010 --test-interval 1 --prerun '/sf/cluster/bin/precorosync.sh' -w '/sf/cluster/sbin/corosync -f') OK!.
```