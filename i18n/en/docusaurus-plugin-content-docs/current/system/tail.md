---
sidebar_position: 1
---

# tail

### Overview

View the end content of specified files in the whitelist and support realtime tracking.

### Command Parameters

```bash
-n      Specify the number of lines displayed at the end, for example: 100
-f      Realtime track new file contents.
<file>  Required parameter specifying file path to view. Only paths in the whitelist are allowed.
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
acli system tail -n 100 /sf/cfg/gpu_info.ini
```

### Output Example

```bash
Mode	  : 0000:15:00.0
Mode	  : 0000:15:00.1
Mode	  : 0000:16:00.0
A100-PCIE-40GB
```
