---
sidebar_position: 1
---

# set

### 操作概述

修改虚拟机磁盘的驱动类型（冷编辑，仅支持关机状态下修改；不指定 --disk-id 则修改全部 ide 族磁盘）

### 命令参数

```bash
-v|--vm-id=string      必要参数，虚拟机ID，示例：614182240912
-t|--type=string       必要参数，目标磁盘驱动类型，枚举值：virtio-blk（virtio 块设备，高性能，需 Guest OS 安装 virtio 驱动）、ide（IDE 兼容模式）、virtio-scsi（ide 槽位上的 virtio-scsi，高性能，需 virtio 驱动），大小写不敏感，示例：virtio-blk
-d|--disk-id=string    可选参数，磁盘ID（UUID），不指定则修改全部 ide 族磁盘（bus∈{1,2,5}），指定单盘时总开关将被置为关闭，示例：01a03ddf-5148-727d-9e9c-e8e581df7088
-o|--operator=string   可选参数，操作人，用于操作审计日志，缺失时后端记 unknown，示例：zhangsan
```

### 使用示例

```bash
acli vm advcfg disktype set -v 614182240912 -t virtio-blk
acli vm advcfg disktype set -v 614182240912 -d 01a03ddf-5148-727d-9e9c-e8e581df7088 -t ide -o zhangsan
```

### 结果示例

```bash
您确定要执行这个操作? (y[es]/n[o]): y
vmID: 614182240912
scope: all
typeBefore: virtio-blk,ide
typeAfter: virtio-blk
useVblkBefore: no
useVblkAfter: yes
realUseVblkBefore: no
realUseVblkAfter: yes
taskID: host-005056b2894b:280998:1760441353:6913569233831
warning: null
```
