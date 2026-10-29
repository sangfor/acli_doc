---
sidebar_position: 1
---

# modinfo

### 操作概述

查询内核模块的文件位置、作者、许可证、依赖及签名等信息。

### 命令参数

命令格式：

```bash
acli system modinfo [options] <module>
```

支持的参数：

本命令采用封闭式只读选项白名单（未列举即拒绝）。

```text
-a|--author=flag        显示作者
-d|--description=flag   显示模块描述
-l|--license=flag       显示许可证
-p|--parameters=flag    显示模块参数信息
-n|--filename=flag      显示模块文件名
-0|--null=flag          使用 NUL 字符分隔输出
-V|--version=flag       显示工具版本
-h|--help=flag          显示帮助信息
-F|--field=string       显示指定字段
-k|--set-version=string 指定要查询的内核版本
<module>               模块名或 .ko 路径，最多 1 个位置参数，例如 ext4
```

版本和帮助查询可不指定模块。

禁止清单：

```text
-b|--basedir=string    改变模块查找根目录，可指向任意目录读取 .ko，拒绝执行
```

modinfo 本身无写能力；这里限制的是读取范围和调用参数。白名单外参数及超过 1 个模块位置参数的调用一律拒绝。

### 使用示例

```bash
acli system modinfo ext4
```

### 结果示例

以下为实际输出节选，签名后续内容省略：

```text
filename:       /lib/modules/6.6.0-99.0.0.102.sfc.7.0.0.0053.sf6.x86_64/kernel/fs/ext4/ext4.ko.xz
softdep:        pre: crc32c
license:        GPL
description:    Fourth Extended Filesystem
author:         Remy Card, Stephen Tweedie, Andrew Morton, Andreas Dilger, Theodore Ts'o and others
alias:          fs-ext4
alias:          ext3
alias:          fs-ext3
alias:          ext2
alias:          fs-ext2
srcversion:     3D72639F7F4812906AEDF83
depends:        jbd2,mbcache
retpoline:      Y
intree:         Y
name:           ext4
vermagic:       6.6.0-99.0.0.102.sfc.7.0.0.0053.sf6.x86_64 SMP mod_unload modversions
sig_id:         PKCS#7
signer:         Cloud kernel signing key
sig_key:        08:1A:F8:80:29:47:CB:D0:E8:72:7D:13:1A:CC:5D:39:C6:B9:12:12
sig_hashalgo:   sha256
signature:      6F:DD:41:45:18:37:2C:72:D7:20:4E:5D:58:81:43:A0:A1:44:DB:5D:
                ...
```
