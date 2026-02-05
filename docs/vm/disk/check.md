---
sidebar_position: 1
---

# check

### 操作概述

使用qcow2-dump工具检查磁盘镜像是否损坏

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机id，示例：3535177259949
-d|--disk=string     必要参数，虚拟机disk名称，示例：vm-disk-1.qcow2
```

### 使用示例

```bash
acli vm disk check -v 2749923911666 -d vm-disk-1.qcow2
```

### 结果示例

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
