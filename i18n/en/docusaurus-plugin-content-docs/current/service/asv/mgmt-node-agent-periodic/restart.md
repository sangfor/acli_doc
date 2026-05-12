---
sidebar_position: 1
---

# restart

### Overview

Restart mgmt-node-agent-periodic service

### Command Parameters

No parameters

### Usage Example

```bash
acli service asv mgmt-node-agent-periodic restart
```

### Output Example

```bash
Stoping mgmt-node-agent-periodic: :checking stop status: getcmdpid return 1, get pids: :  OK!.
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Start (supervisor --lock-file '/var/run/supervisor/mgmt-node-agent-periodic.suplock' --flag-file '*' --flag 011 -w '/sf/bin/mgmt-node-agent-periodic --config-file /sf/etc/mgmt-node-agent/mgmt-node-agent-periodic.conf') OK!.
```