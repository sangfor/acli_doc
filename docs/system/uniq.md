---
sidebar_position: 1
---

# uniq

### 操作概述

过滤并输出文件或输入中相邻的重复行，支持管道输入（只读）。

### 命令参数

本命令为完全只读命令，选项均放通（无选项白名单）；位置参数最多 1 个，且路径须命中 cat 命令族共用路径白名单。

```bash
<file>  可选参数，指定待过滤的文件，至多 1 个；须命中 cat 命令族路径白名单，示例：/var/log/messages
-c      可选参数，在每行前显示该行重复出现的次数，示例：acli system uniq -c /var/log/messages
-d      可选参数，仅显示重复的行
-u      可选参数，仅显示不重复的行
-i      可选参数，比较时忽略大小写
-f <N>  可选参数，比较时跳过每行前 N 个字段
-s <N>  可选参数，比较时跳过每行前 N 个字符
-w <N>  可选参数，每行最多比较前 N 个字符
```

不指定 `<file>` 时从标准输入读取，可配合管道使用。

可过滤的路径白名单（cat 命令族共用：cat/grep/tail/diff 文本查看/比较族，去包含后 81 条，节选）：

文件类（精确匹配，节选）：

```bash
/cfs/.members
/cfs/cfgmaster.ini
/etc/fstab
/etc/hosts
/etc/machine-id
/etc/resolv.conf
/sf/version
```

目录前缀类（前缀匹配，节选）：

```bash
/proc/
/sys/class/net/
/sf/log/
/var/log/
/tmp/
```

通配符类（glob 匹配，节选）：

```bash
/etc/lvm/archive/*.vg
/sf/cfg/vs/disk/*
/boot/grub2/grub.cfg*
```

### 使用示例

```bash
acli system uniq /var/log/messages
```

```bash
acli system uniq -c /var/log/messages
```

### 结果示例

```bash
# acli system uniq /var/log/messages
line a
line b
line c
```