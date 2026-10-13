---
sidebar_position: 1
---

# list

### 操作概述

列出虚拟机全部磁盘及驱动类型（含总开关状态）

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机ID，示例：614182240912
```

### 使用示例

```bash
acli vm advcfg disktype list -v 614182240912
```

### 结果示例

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
