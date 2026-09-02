---
sidebar_position: 1
---

# cat

### Overview

Read and view contents of specified files in system whitelist.

### Command Parameters

```bash
<file>    Required parameter: specify the path of the file to read. Only paths in the whitelist can be viewed. Example: /proc/cpuinfo
```

Viewable path whitelist (file type):

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

Viewable path whitelist (directory prefix type):

```bash
/sf/cfg/if.d/    (e.g. /sf/cfg/if.d/<*>
/sys/class/net/  (e.g. /sys/class/net/<*>
/sf/log/         (e.g. /sf/log/<*>
/var/log/        (e.g. /var/log/<*>
```

### Usage Example

```bash
acli system cat /proc/cpuinfo
```

### Output Example

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
