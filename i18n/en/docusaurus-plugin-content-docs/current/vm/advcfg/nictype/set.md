---
sidebar_position: 1
---

# set

### Overview

Modify the model of the specified NIC on the virtual machine (only supported when the VM is powered off)

### Command Parameters

```bash
-v|--vm-id=string    Required parameter, virtual machine ID, example: 614182240912
-n|--nic-id=string   Required parameter, NIC ID, value is iface_id, example: f2d33928-059a-4cd6-9902-ab39cde9189c
-t|--type=string     Required parameter, target NIC model, enum values: virtio (virtio paravirtualized NIC, better performance, requires virtio driver installed in Guest OS) or e1000 (Intel 82540EM emulated gigabit NIC, better compatibility), case-insensitive, example: virtio
```

### Usage Example

```bash
acli vm advcfg nictype set -v 614182240912 -n f2d33928-059a-4cd6-9902-ab39cde9189c -t virtio
```

### Output Example

```bash
Are you sure you want to perform this operation? (y[es]/n[o]): y
vmID: 614182240912
nicID: f2d33928-059a-4cd6-9902-ab39cde9189c
modelBefore: e1000
modelAfter: virtio
taskID: host-005056b2894b:280998:1760441353:6913569233831
warning: null
```
