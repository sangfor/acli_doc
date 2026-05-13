---
sidebar_position: 1
---

# restart

### Overview

Restart mgmt-node-agent-api service

### Command Parameters

No parameters

### Usage Example

```bash
acli service asv mgmt-node-agent-api restart 
```

### Output Example

```bash
Stoping mgmt-node-agent-api: :checking stop status: getcmdpid return 1, get pids: :  OK!.
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Start (supervisor --lock-file '/var/run/supervisor/mgmt-node-agent-api.suplock' --flag-file '*' --flag 011 -w '/sf/bin/mgmt-node-agent-api --config-file /sf/etc/mgmt-node-agent/mgmt-node-agent-api.conf') OK!.
```