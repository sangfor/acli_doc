---
sidebar_position: 1
---

# start

### Overview

Monitoring (disk IO, VS IO, virtual machine IO, pidstat, network) information stored in files

### Command Parameters

```bash
-c|--core=string             Monitoring item, monitor CPU information; example: '1,2,3', all cores 'all'
-s|--disk=string             Monitoring item, monitor disk devices; example: 'sda,sdb', all disks 'all'
-d|--duration=integer        Monitoring time in days (default: 1)
-f|--frequency=integer       Monitoring frequency in seconds (default: 2)
-n|--net=string              Monitoring item, monitor network card information; example: 'eth1,eth2', all network cards 'all'
-p|--pid=string              Monitoring item, monitor process information; example: 'pid1,pid2', all processes 'all'
-v|--vm=string               Monitoring item, monitor VM information; specify VM vmid, currently only supports one vmid
-i|--vs=bool                 Monitoring item, monitor virtual storage
--lang=string                Set the command line output language, options are zh_CN and en_US
-h|--help                    Display help information
```

### Usage Example

```bash
# Example 1: Monitor specified disk devices
acli performance_tools monitor start -s sda,sdb

# Example 2: Monitor all disk devices
acli performance_tools monitor start -s all
```

### Output Example

```bash
Program started, pid: 1337319
```
