---
sidebar_position: 1
---

# grep

### 操作概述

在白名单内的配置或系统文件中按关键字搜索匹配行

### 命令参数

```bash
-E         使用扩展正则表达式进行匹配
-i         忽略大小写
-v         反向匹配，输出不匹配的行
-n         显示匹配行的行号
-r         递归搜索指定目录
-c         只输出匹配的总行数
-F         将模式视为固定字符串
-P         使用 Perl 兼容正则表达式
<pattern>  必要参数，要搜索的关键字或正则表达式
<file>     必要参数，要搜索的文件或目录，仅允许白名单内的路径
```

可搜索的路径白名单（cat 命令族共用：cat/grep/tail/diff 文本查看/比较族，去包含后 81 条，节选）：

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
acli system grep -n "eth0" /proc/interrupts
```

### 结果示例

```bash
# acli system grep -n "eth0" /proc/interrupts
 30:      0      0      0      0    6452280   eth0-0
 63:      0      0      0      0    8388608   eth0.1-0
```
