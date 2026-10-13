---
sidebar_position: 1
---

# list

### Overview

List all device-level multipath custom policies on the specified node, each with custom params and matched storages.

### Command Parameters

```bash
-n|--hostname=string    Optional parameter, target host name. Defaults to the current node. Example: host-xxxx
```

### Usage Example

```bash
acli system multipathconfig devicepolicy list -n host-xxxx
```

### Output Example

```bash
    custom_params                |product        |storages                                             |vendor 
    -----------------------------|---------------|-----------------------------------------------------|-------
1   path_checker readsector0     |PowerStore|368ccf09800fec26a86bd45b6b76bc498 (PowerStore-01)    |DellEMC
    path_grouping_policy failover|               |                                                     |
```
