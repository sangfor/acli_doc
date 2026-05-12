---
sidebar_position: 1
---

# restart

### Overview

Restart the vn-manager-service-api service

### Command Parameters

No parameters

### Usage Example

```bash
acli service anet vn-manager-service-api restart
```

### Output Example

```bash
Stoping vn-manager-service-api: : .  OK!.
Start (supervisor --flag-file '/var/run/vn-manager-service-api.pid' --flag 010 -p '/sf/vn/bin/vn-manager-service-api --config-file /sf/vn/etc/vn-manager-service/vn-manager-service-api.conf',*vn-manager-service-api*) OK!.
```