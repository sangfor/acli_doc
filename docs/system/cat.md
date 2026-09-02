---
sidebar_position: 1
---

# cat

### 操作概述

读取并查看系统白名单内指定文件的内容

### 命令参数

```bash
<file>    必要参数，指定要读取的文件路径，仅允许查看白名单内的路径，示例：/proc/cpuinfo
```

可查看的路径白名单（文件类）：

```bash
/cfs/cfgmaster.ini
/cfs/.members
/sf/version
/sys/class/dmi/id/sys_vendor
/proc/cpuinfo
/proc/meminfo
/proc/interrupts
/sf/cfg/gpu_info.ini
```

可查看的路径白名单（目录前缀类）：

```bash
/sf/cfg/if.d/    （如 /sf/cfg/if.d/<*>）
/sys/class/net/  （如 /sys/class/net/<*>）
/sf/log/         （如 /sf/log/<*>）
/var/log/        （如 /var/log/<*>）
```

### 使用示例

```bash
acli system cat /proc/cpuinfo
```

### 结果示例

```bash
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 85
model name	: Intel(R) Xeon(R) Gold 5220R CPU @ 2.20GHz
stepping	: 7
microcode	: 0x500320a
cpu MHz		: 2200.000
cache size	: 36608 KB
...
```
