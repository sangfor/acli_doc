---
sidebar_position: 1
---

# set

### Overview

Modify the driver type of the virtual machine disk (cold edit, only supported when the VM is powered off; if --disk-id is not specified, all ide-family disks will be modified)

### Command Parameters

```bash
-v|--vm-id=string      Required parameter, virtual machine ID, example: 614182240912
-t|--type=string       Required parameter, target disk driver type, enum values: virtio-blk (virtio block device, high performance, requires virtio driver installed in Guest OS), ide (IDE compatibility mode), virtio-scsi (virtio-scsi on IDE slot, high performance, requires virtio driver), case-insensitive, example: virtio-blk
-d|--disk-id=string    Optional parameter, disk ID (UUID). If not specified, all ide-family disks (bus in {1,2,5}) will be modified; when a single disk is specified, the master switch will be turned off, example: 01a03ddf-5148-727d-9e9c-e8e581df7088
-o|--operator=string   Optional parameter, operator, used for operation audit logs; when missing, the backend records 'unknown', example: zhangsan
```

### Usage Example

```bash
acli vm advcfg disktype set -v 614182240912 -t virtio-blk
acli vm advcfg disktype set -v 614182240912 -d 01a03ddf-5148-727d-9e9c-e8e581df7088 -t ide -o zhangsan
```

### Output Example

```bash
Are you sure you want to perform this operation? (y[es]/n[o]): y
vmID: 614182240912
scope: all
typeBefore: virtio-blk,ide
typeAfter: virtio-blk
useVblkBefore: no
useVblkAfter: yes
realUseVblkBefore: no
realUseVblkAfter: yes
taskID: host-005056b2894b:280998:1760441353:6913569233831
warning: null
```
