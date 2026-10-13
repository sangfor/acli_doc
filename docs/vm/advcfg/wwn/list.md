---
sidebar_position: 1
---

# list

### 操作概述

列出虚拟机全部磁盘及 WWN

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机ID，示例：614182240912
```

### 使用示例

```bash
acli vm advcfg wwn list -v 614182240912
```

### 结果示例

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