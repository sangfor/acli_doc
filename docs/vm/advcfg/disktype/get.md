---
sidebar_position: 1
---

# get

### 操作概述

查询虚拟机指定磁盘的驱动类型

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机ID，示例：614182240912
-d|--disk-id=string  必要参数，磁盘ID（UUID），示例：01a03ddf-5148-727d-9e9c-e8e581df7088
```

### 使用示例

```bash
acli vm advcfg disktype get -v 614182240912 -d 01a03ddf-5148-727d-9e9c-e8e581df7088
```

### 结果示例

```bash
vmID: 614182240912
diskID: 01a03ddf-5148-727d-9e9c-e8e581df7088
slot: ide0
bus: 2
busName: ide
bootdisk: true
diskName: IDE1
sizeGib: 100
```
