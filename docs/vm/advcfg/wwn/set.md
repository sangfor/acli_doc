---
sidebar_position: 1
---

# set

### 操作概述

修改虚拟机磁盘的 WWN（冷编辑，仅支持关机状态下修改；仅支持 virtio-scsi 总线磁盘设置非空 WWN）

### 命令参数

```bash
-v|--vm-id=string      必要参数，虚拟机ID，示例：614182240912
-d|--disk-id=string    必要参数，磁盘ID（UUID），示例：01a03ddf-5148-727d-9e9c-e8e581df7088（可用 vm advcfg wwn list 获取）
-w|--wwn=string        必要参数，磁盘WWN（32位十六进制字符，不含 0x 前缀），示例：6000c29a3b7e4f18a1b2c3d4e5f60718；空串表示清除 WWN
```

### 使用示例

```bash
acli vm advcfg wwn set -v 614182240912 -d 01a03ddf-5148-727d-9e9c-e8e581df7088 -w 6000c29a3b7e4f18a1b2c3d4e5f60718
acli vm advcfg wwn set -v 614182240912 -d 01a03ddf-5148-727d-9e9c-e8e581df7088 -w ""
```

### 结果示例

```bash
您确定要执行这个操作? (y[es]/n[o]): y
vmID: 614182240912
diskID: 01a03ddf-5148-727d-9e9c-e8e581df7088
wwnBefore: 6000c29a3b7e4f18a1b2c3d4e5f60718
wwnAfter: 6000c2947d4742619d88eb6f9fbf6ed2
```