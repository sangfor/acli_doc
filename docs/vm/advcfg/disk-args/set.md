---
sidebar_position: 1
---

# set

### 操作概述

修改虚拟机磁盘的自定义 qemu 开机参数（冷编辑，仅支持关机状态下修改）

### 命令参数

```bash
-v|--vm-id=string        必要参数，虚拟机ID，示例：6520699837375
-t|--type=string         必要参数，作用粒度，枚举值：vm（修改虚拟机全部磁盘）、disk（仅修改 --disk-id 指定的单个磁盘），大小写不敏感，示例：disk。仅支持关机状态下修改
-d|--disk-id=string      可选参数，磁盘ID（UUID），示例：01a0b267-4842-7f0b-8e18-864986d2e3da。--type disk 时必须指定；--type vm 时忽略
-D|--drive-args=string   可选参数，自定义 qemu -drive 串尾参数（裸逗号分隔），示例：iothread=iothread0,copy-on-read=on。整体覆盖：传值则替换，传空串则清空该字段；不传则保持该字段不变。注意：值以 - 开头时必须用 = 形式传参，值中不能包含高危 Linux 命令字样，否则会被安全控制拦截
-a|--device-args=string  可选参数，自定义 qemu -device 串尾参数（裸逗号分隔），示例：serial=SN-001。整体覆盖：传值则替换，传空串则清空该字段；不传则保持该字段不变。注意：值以 - 开头时必须用 = 形式传参，值中不能包含高危 Linux 命令字样，否则会被安全控制拦截
```

### 使用示例

```bash
# 修改单个磁盘
acli vm advcfg disk-args set -v 6520699837375 -t disk -d 01a0b267-4842-7f0b-8e18-864986d2e3da -D "iothread=iothread0,copy-on-read=on" -a "serial=SN-001"
# 批量修改全部磁盘（仅改 -drive 参数）
acli vm advcfg disk-args set -v 6520699837375 -t vm -D "iothread=iothread0"
```

### 结果示例

修改单个磁盘（`--type disk`）：

```bash
您确定要执行这个操作? (y[es]/n[o]): y
diskID: 01a0b267-4842-7f0b-8e18-864986d2e3da
diskIDs:
  [0]: 01a0b267-4842-7f0b-8e18-864986d2e3da
perDiskChanges:
  [0]:
    deviceArgsAfter: serial=SN-001
    deviceArgsBefore:
    diskID: 01a0b267-4842-7f0b-8e18-864986d2e3da
    driveArgsAfter: iothread=iothread0,copy-on-read=on
    driveArgsBefore:
    slot: ide0
scope: disk
vmID: 6520699837375
```

批量修改全部磁盘（`--type vm`）：

```bash
您确定要执行这个操作? (y[es]/n[o]): y
diskIDs:
  [0]: 01a0b267-4842-7f0b-8e18-864986d2e3da
perDiskChanges:
  [0]:
    deviceArgsAfter:
    deviceArgsBefore:
    diskID: 01a0b267-4842-7f0b-8e18-864986d2e3da
    driveArgsAfter: iothread=iothread0
    driveArgsBefore:
    slot: ide0
scope: vm
vmID: 6520699837375
```