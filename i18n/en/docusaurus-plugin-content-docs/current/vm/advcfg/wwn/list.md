---
sidebar_position: 1
---

# list

### Overview

List all disks of the virtual machine and their WWNs

### Command Parameters

```bash
-v|--vm-id=string      Required parameter, virtual machine ID, example: 614182240912
```

### Usage Example

```bash
acli vm advcfg wwn list -v 614182240912
```

### Output Example

```bash
vmID: 614182240912
disks:
  - diskID: 01a03ddf-5148-727d-9e9c-e8e581df7088
    diskName: VirtioScsi0
    busName: virtio-scsi
    bootdisk: true
    wwn: 6000c29a3b7e4f18a1b2c3d4e5f60718
  - diskID: 9e9ce8e5-8172-4d7d-5148-01a03ddf7088
    diskName: Virtio0
    busName: virtio
    bootdisk: false
    wwn: ""
```