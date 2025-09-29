---
sidebar_position: 10
---

# smartctl
操作概述: 调用系统smartctl命令

命令参数:
```bash
无
```

使用示例:
```bash
acli system smartctl
```

结果示例:
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