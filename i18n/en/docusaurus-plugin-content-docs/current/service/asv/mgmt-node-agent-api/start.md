---
sidebar_position: 1
---

# start

### Overview

Start mgmt-node-agent-api service

### Command Parameters

No parameters

### Usage Example

```bash
acli service asv mgmt-node-agent-api start
```

### Output Example

```bash
Physical cores < 16: 8checking before start: getcmdpid return 0, get pids: 903065 903069:checking before start: getcmdpid2 return 1, get pids: :Start (supervisor --lock-file '/var/run/supervisor/mgmt-node-agent-api.suplock' --flag-file '*' --flag 011 -w '/sf/bin/mgmt-node-agent-api --config-file /sf/etc/mgmt-node-agent/mgmt-node-agent-api.conf') OK!.
```