---
sidebar_position: 1
---

# get

### Overview

Query the driver type of the specified disk of the virtual machine

### Command Parameters

```bash
-v|--vm-id=string    Required parameter, virtual machine ID, example: 614182240912
-d|--disk-id=string  Required parameter, disk ID (UUID), example: 01a03ddf-5148-727d-9e9c-e8e581df7088
```

### Usage Example

```bash
acli vm advcfg disktype get -v 614182240912 -d 01a03ddf-5148-727d-9e9c-e8e581df7088
```

### Output Example

```bash
vmID: 614182240912
diskID: 01a03ddf-5148-727d-9e9c-e8e581df7088
slot: ide0
bus: 2
busName: ide
bootdisk: true
diskName: IDE1
sizeGib: 100
```
