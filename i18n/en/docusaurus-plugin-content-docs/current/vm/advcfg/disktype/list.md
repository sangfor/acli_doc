---
sidebar_position: 1
---

# list

### Overview

List all disks and their driver types of the virtual machine (including the master switch status)

### Command Parameters

```bash
-v|--vm-id=string    Required parameter, virtual machine ID, example: 614182240912
```

### Usage Example

```bash
acli vm advcfg disktype list -v 614182240912
```

### Output Example

```bash
vmID: 614182240912
useVblk: no
realUseVblk: no
disks:
  - diskID: 01a03ddf-5148-727d-9e9c-e8e581df7088
    slot: ide0
    bus: 2
    busName: ide
    bootdisk: true
    diskName: IDE1
  - diskID: 9e9ce8e5-8172-4d7d-5148-01a03ddf7088
    slot: scsi0
    bus: 5
    busName: virtio-scsi
    bootdisk: false
    diskName: SCSI0
```
