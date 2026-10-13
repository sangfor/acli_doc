---
sidebar_position: 1
---

# get

### Overview

Query the effective multipath policy for the specified storage on the specified node

### Command Parameters

```bash
-n|--hostname=string    Optional parameter, target host name. Defaults to the current node. Example: host-xxxx
-w|--wwid=string         Required parameter, logical storage WWID. Example: 3648bd4a100fa95b6550a2d9c000002ac
```

### Usage Example

```bash
acli system multipathconfig get -n host-xxxx -w 3648bd4a100fa95b6550a2d9c000002ac
```

### Output Example

```bash
    device                       |multipath
    -----------------------------|---------
1   path_checker readsector0     |         
    path_grouping_policy failover|         
    product PowerStore      |         
    vendor DellEMC               |
```
