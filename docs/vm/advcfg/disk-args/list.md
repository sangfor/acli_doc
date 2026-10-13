---
sidebar_position: 1
---

# list

### 操作概述

列出虚拟机全部磁盘及自定义 qemu 开机参数

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机ID，示例：6520699837375
```

### 使用示例

```bash
acli vm advcfg disk-args list -v 6520699837375
```

### 结果示例

```bash
disks:
  [0]:
    deviceArgs:
    diskID: 01a0b267-4842-7f0b-8e18-864986d2e3da
    diskName: opencloud-disk-0-20260918
    driveArgs:
    slot: ide0
vmID: 6520699837375
```