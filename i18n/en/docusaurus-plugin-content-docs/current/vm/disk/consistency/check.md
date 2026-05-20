---
sidebar_position: 1
---

# check

### Overview

Check disk consistency, compare path and size_gib fields between database and CFS config

### Command Parameters

```bash
-v|--vm-id=string    Required parameter, VM ID. Example: 5694620180825
-d|--disk-id=string  Optional parameter, disk ID, if not specified, all disks in the VM will be checked. Example: 019e3927-3911-7af1-9768-abb3cd79aa98
```

### Usage Example

```bash
# Check all disks in VM
acli vm disk consistency check -v 5694620180825

# Check specific disk
acli vm disk consistency check -v 5694620180825 -d 019e3927-3911-7af1-9768-abb3cd79aa98
```

### Output Example

```bash
{"code":0,"data":{"checkResult":{"019e3927-3911-7af1-9768-abb3cd79aa98":{"path":{"dbPath":"/disks/ab/b3/019e3927-3911-7af1-9768-abb3cd79aa98/019e3927-3911-7af1-9768-abb3cd79aa98.qcow2","cfsPath":"/disks/ab/b3/019e3927-3911-7af1-9768-abb3cd79aa98/019e3927-3911-7af1-9768-abb3cd79aa98.qcow2","match":true},"size":{"dbSizeGib":10,"cfsSizeGib":10,"match":true}}}}}
```