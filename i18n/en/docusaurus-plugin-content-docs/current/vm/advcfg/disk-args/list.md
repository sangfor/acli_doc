---
sidebar_position: 1
---

# list

### Overview

List all disks and their custom QEMU args of the VM

### Command Parameters

```bash
-v|--vm-id=string    Required parameter, virtual machine ID, example: 6520699837375
```

### Usage Example

```bash
acli vm advcfg disk-args list -v 6520699837375
```

### Output Example

```bash
disks:
  [0]:
    deviceArgs:
    diskID: 01a0b267-4842-7f0b-8e18-864986d2e3da
    diskName: opencloud-disk-0-20260918
    driveArgs:
    slot: ide0
vmID: 6520699837375
```