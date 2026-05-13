---
sidebar_position: 1
---

# restart

### Overview

Restart the vn-node-agent-api service

### Command Parameters

No parameters

### Usage Example

```bash
acli service anet vn-node-agent-api restart
```

### Output Example

```bash
Stoping vn-node-agent-api: : .  OK!.
Start (supervisor --flag-file '/var/run/vn-node-agent-api.pid' --flag 010 -p '/sf/vn/bin/vn-node-agent-api --config-file /sf/vn/etc/vn-node-agent/vn-node-agent-api.conf',*vn-node-agent-api*) OK!.
```