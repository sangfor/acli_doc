---
sidebar_position: 1
---

# get

### 操作概述

查询虚拟机指定磁盘的自定义 qemu 开机参数

### 命令参数

```bash
-v|--vm-id=string      必要参数，虚拟机ID，示例：6520699837375
-d|--disk-id=string    必要参数，磁盘ID（UUID），示例：01a0b267-4842-7f0b-8e18-864986d2e3da（可用 vm advcfg disk-args list 获取）
```

### 使用示例

```bash
acli vm advcfg disk-args get -v 6520699837375 -d 01a0b267-4842-7f0b-8e18-864986d2e3da
```

### 结果示例

未设置时：

```bash
deviceArgs:
diskID: 01a0b267-4842-7f0b-8e18-864986d2e3da
diskName: opencloud-disk-0-20260918
driveArgs:
slot: ide0
vmID: 6520699837375
```

已设置时：

```bash
deviceArgs: serial=SN-001
diskID: 01a0b267-4842-7f0b-8e18-864986d2e3da
diskName: opencloud-disk-0-20260918
driveArgs: iothread=iothread0,copy-on-read=on
slot: ide0
vmID: 6520699837375
```