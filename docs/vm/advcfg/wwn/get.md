---
sidebar_position: 1
---

# get

### 操作概述

查询虚拟机指定磁盘的 WWN（磁盘唯一标识）

### 命令参数

```bash
-v|--vm-id=string      必要参数，虚拟机ID，示例：614182240912
-d|--disk-id=string    必要参数，磁盘ID（UUID），示例：01a03ddf-5148-727d-9e9c-e8e581df7088（可用 vm advcfg wwn list 获取）
```

### 使用示例

```bash
acli vm advcfg wwn get -v 614182240912 -d 01a03ddf-5148-727d-9e9c-e8e581df7088
```

### 结果示例

```bash
vmID: 614182240912
disk:
  diskID: 01a03ddf-5148-727d-9e9c-e8e581df7088
  diskName: VirtioScsi0
  busName: virtio-scsi
  bootdisk: true
  wwn: 6000c29a3b7e4f18a1b2c3d4e5f60718
```