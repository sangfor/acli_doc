---
sidebar_position: 1
---

# cat

### 操作概述

读取并查看系统白名单内指定文件的内容

### 命令参数

```bash
<file>  必要参数，指定要读取的文件路径，仅允许查看白名单内的路径，示例：/etc/hosts
```

可查看的路径白名单（cat 命令族共用：cat/grep/tail/diff 文本查看/比较族，去包含后 81 条，节选）：

文件类（精确匹配，节选）：

```bash
/cfs/.members
/cfs/cfgmaster.ini
/cfs/cluster.ini
/cfs/storage.cfg
/etc/fstab
/etc/hosts
/etc/issue
/etc/machine-id
/etc/resolv.conf
/sf/version
/sf/vs/version
/sys/class/dmi/id/sys_vendor
/root/.bash_history
/var/log/sfvt_p2vagt.log
```

目录前缀类（前缀匹配，节选）：

```bash
/proc/                 （如 /proc/cpuinfo、/proc/meminfo、/proc/interrupts）
/etc/sysconfig/        （如 /etc/sysconfig/<*>）
/sys/class/net/        （如 /sys/class/net/<*>）
/sys/bus/pci/devices/  （如 /sys/bus/pci/devices/<*>）
/sf/log/               （如 /sf/log/<*>）
/var/log/              （如 /var/log/<*>）
/tmp/                  （如 /tmp/<*>）
```

通配符类（glob 匹配，节选）：

```bash
/etc/lvm/archive/*.vg
/sf/cfg/vs/disk/*
/sys/devices/system/edac/mc/mc*/csrow*/ch*
/boot/grub2/grub.cfg*
```

### 使用示例

```bash
acli system cat /etc/hosts
```

### 结果示例

```bash
# acli system cat /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
```
