---
sidebar_position: 1
---

# repair

### 操作概述

修复共享盘扩容异常。根据指定的共享盘名称，执行底层工具恢复操作，方便故障排查。

### 命令参数

```bash
-n|--name=string        必填，共享盘的名称，示例：my-shared-disk

```

### 使用示例

```bash
acli vm shareddisk repair --name my-shared-disk
acli vm shareddisk repair -n my-shared-disk
```

### 结果示例

```bash
Start recover shared disk, diskID=, diskName=111
Found disk: id=019d950e-efc4-7c80-bce5-369417427f43, name=111, storageId=1SANGFOR_ASAN-03d-8c51-4bbb-b896-281d5a83382a, path=/disks/36/94/019d950e-efc4-7c80-bce5-369417427f43/019d950e-efc4-7c80-bce5-369417427f43.raw
Disk is normal, no need to repair: /sf/data/1SANGFOR_ASAN-03d-8c51-4bbb-b896-281d5a83382a/disks/36/94/019d950e-efc4-7c80-bce5-369417427f43/019d950e-efc4-7c80-bce5-369417427f43.raw
Success to recover extending shared disk: 019d950e-efc4-7c80-bce5-369417427f43
```