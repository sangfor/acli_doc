---
sidebar_position: 1
---

# start

### Overview

Start mgmt-node-agent-periodic service

### Command Parameters

No parameters

### Usage Example

```bash
acli service asv mgmt-node-agent-periodic start
```

### Output Example

```bash
 Physical cores < 16: 8checking before start: getcmdpid return 0, get pids: 963439 963442:checking before start: getcmdpid2 return 1, get pids: :Start (supervisor --lock-file '/var/run/supervisor/mgmt-node-agent-periodic.suplock' --flag-file '*' --flag 011 -w '/sf/bin/mgmt-node-agent-periodic --config-file /sf/etc/mgmt-node-agent/mgmt-node-agent-periodic.conf') OK!.
```