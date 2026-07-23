---
sidebar_position: 1
---

# clear

### Overview

Clear device-level multipath custom configuration for the specified vendor/product on the specified node.

### Command Parameters

```bash
-n|--hostname=string    Optional parameter, target host name. Defaults to the current node. Example: host-xxxx
-v|--vendor=string     Required parameter, multipath.conf vendor field. Example: DellEMC
-p|--product=string    Required parameter, multipath.conf product field. Example: PowerStore
```

### Usage Example

```bash
acli system multipathconfig devicepolicy clear -n host-xxxx -v DellEMC -p PowerStore
```

### Output Example

```bash
affected_storages:
  [0]: 3648bd4a100fa95b6550a2d9c000002ac
  [1]: 3648bd4a100fa95b6550a2d9c000002ad
```
