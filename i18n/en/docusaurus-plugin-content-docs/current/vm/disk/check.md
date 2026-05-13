---
sidebar_position: 1
---

# check

### Overview

Check whether the disk image is damaged by using the qcow2-dump tool

### Command Parameters
```bash
-v|--vm-id=string           Required parameter, VM ID, Example: 3535177259949
-d|--disk=string            Required parameter, VM disk name, Example: vm-disk-1.qcow2
```

### Usage Example

```bash
acli vm disk check -v 2749923911666 -d vm-disk-1.qcow2
```

### Output Example

```bash
File: vm-disk-1.qcow2
--------------------------------------------------------------------------
magic: 0x514649fb
version: 3
backing_file_offset: 0x0
backing_file_size: 0
fs_type: nfs
virtual_size: 128849018880 / 122880M / 120G
disk_size: 134217728 / 128M / 0G
seek_end: 134217728 [0x8000000] / 128M / 0G
cluster_bits: 16
cluster_size: 65536
crypt_method: 0
csize_shift: 54
csize_mask: 255
cluster_offset_mask: 0x3fffffffffffff
....
....

##########################################################################
######             Haha:  qcow2 image is good!  Y(^_^)Y             ######
##########################################################################
```