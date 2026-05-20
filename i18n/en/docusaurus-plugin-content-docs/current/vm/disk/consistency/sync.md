---
sidebar_position: 2
---

# sync

### Overview

Sync disk configuration, modify CFS and DB simultaneously based on the provided path and size (Dangerous operation: will overwrite existing configuration)

### Command Parameters

```bash
-v|--vm-id=string    Required parameter, VM ID. Example: 5694620180825
-d|--disk-id=string  Required parameter, disk ID. Example: 019e3927-3911-7af1-9768-abb3cd79aa98
-p|--path=string     Optional parameter, force specify path. Example: /cfs/nodes/5694620180825/test.qcow2
-s|--size=integer    Optional parameter, force specify size in GiB. Example: 100
```

### Usage Example

```bash
# Sync path only (CFS and DB)
acli vm disk consistency sync -v 5694620180825 -d 019e3927-3911-7af1-9768-abb3cd79aa98 -p /cfs/nodes/5694620180825/test.qcow2

# Sync size only (CFS and DB)
acli vm disk consistency sync -v 5694620180825 -d 019e3927-3911-7af1-9768-abb3cd79aa98 -s 100

# Sync both path and size
acli vm disk consistency sync -v 5694620180825 -d 019e3927-3911-7af1-9768-abb3cd79aa98 -p /disks/ab/b3/019e3927-3911-7af1-9768-abb3cd79aa98/019e3927-3911-7af1-9768-abb3cd79aa98.qcow2 -s 10
```

### Output Example

```bash
Are you sure you want to execute the operation? (y[es]/n[o]): y
{"diskID":"019e3927-3911-7af1-9768-abb3cd79aa98","pathBefore":"/disks/ab/b3/019e3927-3911-7af1-9768-abb3cd79aa98/019e3927-3911-7af1-9768-abb3cd79aa98.qcow2","pathAfter":"/disks/ab/b3/019e3927-3911-7af1-9768-abb3cd79aa98/019e3927-3911-7af1-9768-abb3cd79aa98.qcow2","sizeGibBefore":10,"sizeGibAfter":10}
```