---
sidebar_position: 1
---

# fdisk

### 操作概述

查看磁盘分区信息（只读）。

### 命令参数

本命令为部分只读命令，采用封闭式参数白名单（仅列举的参数允许，其余拒绝）。

```bash
-l|--list=flag  可选参数，列出指定设备的分区信息（仅允许白名单内路径），示例：acli system fdisk -l /dev/sda
```

可查询的路径白名单（dev 命令族路径白名单，仅 1 条，即 /dev/ 目录）：

```bash
/dev/  （块设备目录，支持前缀匹配，如 /dev/sda）
```

写参数禁止清单（命中即拒绝）：

```bash
无 -l 时进入交互式分区菜单（可写磁盘）  交互式分区菜单，可写磁盘
n/d/w/t/a/m/p（交互命令）    交互命令：new/delete/write/type/toggle/menu/print
```

### 使用示例

```bash
acli system fdisk -l /dev/sda
```

### 结果示例

```bash
# acli system fdisk -l /dev/sda
Disk /dev/sda: 1.8 TiB, 2000398934016 bytes, 3907029168 sectors
Disk model: SATA SSD
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: gpt
Disk identifier: 12345678-90AB-CDEF-1234-567890ABCDEF

Device       Start        End    Sectors   Size Type
/dev/sda1     2048    2099199    2097152     1G EFI System
/dev/sda2  2099200  3907028991 3904929792   1.8T Linux filesystem
```
