---
sidebar_position: 1
---

# set

### Overview

Modify multipath policy

### Command Parameters

```bash
-w|--wwid=string                     Required parameter, logical storage ID, example: 3648bd4a100fa95b6550a2d9c000002ac
-n|--nodes=string                    Required parameter, host ID list, multiple nodes separated by commas, example: host-0050568eefd7,host-a416e704e387
-g|--path-grouping-policy=string     Required parameter, path grouping policy, failover(Active/Standby), multibus(Load Balancing), group_by_prio(Group by priority), group_by_serial(Group by serial), group_by_node_name(Group by node name)
```

### Usage Example

```bash
acli system multipathconfig set -w 3648bd4a100fa95b6550a2d9c000002ac -n host-0050568eefd7,host-a416e704e387 -g failover
```

### Output Example

```bash
UPID:host-005056b22c8d:00276CFF:BD680A:6A18ED61:设置多路径策略::admin@vtp:
```
