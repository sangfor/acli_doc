---
sidebar_position: 1
---

# smartctl

### Overview

smartctl command

### Command Parameters

```bash
-i|--info=flag             Display device ID information
-H|--health=flag           Display device health status
-A|--attributes=flag       Display SMART attributes of display device
-a|--all=flag              Display all SMART information of display device
-x|--xall=flag             Display all information of display device
-j|--json=flag             Output as JSON
-l                         Query logs of specified types. Value can be any value. Example: error, selftest
-d                         Specify device type. Value can be any value. Example: scsi
-T|--tolerance=string      Fault tolerance mode, value is fixed as permissive.
<disk>                     Mandatory parameter for specifying a disk device. The path must be limited to /dev/sd[a-z]+. Example: /dev/sda
```

### Usage Example

```bash
acli system smartctl -i /dev/sda
```

```bash
acli system smartctl -H /dev/sda
```

```bash
acli system smartctl -a /dev/sda
```

### Output Example

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