---
sidebar_position: 1
---

# list

### Overview

Get current health status of services in network configuration channel

### Command Parameters
```bash
-c|--cache=string    Query from cache: 0 (Real-time Query), 1 (Query from Cache), Enum values: 0,1
```

### Usage Example

```bash
acli network anet config configchannel serviceinfo list --cache 0
```

### Output Example

```bash
    host             |service           |status
    -----------------|------------------|-------
1   host-005056b223bc|vn-lcp            |Healthy
2   null             |kafka             |Healthy
3   host-005056b2d4e1|vn-lcp            |Healthy
4   host-005056b2d4f1|vn-lcp            |Healthy
5   null             |vn-ccp            |Healthy
6   null             |vn-manager-service|Healthy
```