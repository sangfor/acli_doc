---
sidebar_position: 1
---

# smartctl

### 操作概述

smartctl命令

### 命令参数

```bash
-i|--info=flag             显示设备的标识信息
-H|--health=flag           显示设备的健康状态
-A|--attributes=flag       显示设备的 SMART 属性
-a|--all=flag              显示设备的全部 SMART 信息
-x|--xall=flag             显示设备的全部信息
-j|--json=flag             以 JSON 格式输出
-l                         查询指定类型的日志，<值> 取值不限，示例：error、selftest
-d                         指定设备类型，<值> 取值不限，示例：scsi
-T|--tolerance=string      容错模式，值固定为 permissive
<disk>                     必要参数，指定磁盘设备，路径限 /dev/sd[a-z]+，示例：/dev/sda
```

### 使用示例

```bash
acli system smartctl -i /dev/sda
```

```bash
acli system smartctl -H /dev/sda
```

```bash
acli system smartctl -a /dev/sda
```

### 结果示例

```bash
# acli system smartctl -h
smartctl 6.6 2017-11-05 r4594 [x86_64-linux-4.18.0-6.11.1] (local build)
Copyright (C) 2002-17, Bruce Allen, Christian Franke, www.smartmontools.org

Usage: smartctl [options] device

============================================ SHOW INFORMATION OPTIONS =====

  -h, --help, --usage
         Display this help and exit

  -V, --version, --copyright, --license
         Print license, copyright, and version information and exit

  -i, --info
         Show identity information for device

  --identify[=[w][nvb]]
         Show words and bits from IDENTIFY DEVICE data                (ATA)

  -g NAME, --get=NAME
        Get device setting: all, aam, apm, dsn, lookahead, security,
        wcache, rcache, wcreorder, wcache-sct

  -a, --all
         Show all SMART information for device

  -x, --xall
         Show all information for device

  --scan
         Scan for devices

  --scan-open
         Scan for devices and try to open each device
```
