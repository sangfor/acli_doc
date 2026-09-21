---
sidebar_position: 1
---

# set

### Overview

Modify the WWN of the virtual machine disk (cold edit, only supported when the VM is powered off; only virtio-scsi bus disks support setting a non-empty WWN)

### Command Parameters

```bash
-v|--vm-id=string      Required parameter, virtual machine ID, example: 614182240912
-d|--disk-id=string    Required parameter, disk ID (UUID), example: 01a03ddf-5148-727d-9e9c-e8e581df7088 (obtainable via vm advcfg wwn list)
-w|--wwn=string        Required parameter, disk WWN (32 hexadecimal characters, without 0x prefix), example: 6000c29a3b7e4f18a1b2c3d4e5f60718; an empty string clears the WWN
```

### Usage Example

```bash
acli vm advcfg wwn set -v 614182240912 -d 01a03ddf-5148-727d-9e9c-e8e581df7088 -w 6000c29a3b7e4f18a1b2c3d4e5f60718
acli vm advcfg wwn set -v 614182240912 -d 01a03ddf-5148-727d-9e9c-e8e581df7088 -w ""
```

### Output Example

```bash
Are you sure you want to execute the operation? (y[es]/n[o]): y
vmID: 614182240912
diskID: 01a03ddf-5148-727d-9e9c-e8e581df7088
wwnBefore: 6000c29a3b7e4f18a1b2c3d4e5f60718
wwnAfter: 6000c2947d4742619d88eb6f9fbf6ed2
```