---
sidebar_position: 1
---

# tail

### 操作概述

查看白名单内指定文件的末尾内容，支持实时跟踪

### 命令参数

```bash
-n      指定显示末尾的行数，示例：100
-f      实时跟踪文件新增内容
<file>  必要参数，指定要查看的文件路径，仅允许白名单内的路径
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
acli system tail -n 100 /sf/cfg/gpu_info.ini
```

### 结果示例

```bash
Mode	  : 0000:15:00.0
Mode	  : 0000:15:00.1
Mode	  : 0000:16:00.0
A100-PCIE-40GB
```
