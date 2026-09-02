---
sidebar_position: 1
---

# grep

### Overview

Search for matching lines by keyword in configuration files or system files that are whitelisted.

### Command Parameters

```bash
-E         Use extended regular expressions for matching.
-i         Ignore case
-v         Reverse match, output unmatched lines
-n         Display line numbers of matched lines
-r         Recursively search specified directory
-c         Output total matched lines only
-F         Treat pattern as fixed string
-P         Use Perl-compatible regular expressions
<pattern>  Required parameter: keyword or regular expression to search for.
<file>     Required parameter: file/directory to search for; only paths in the whitelist are allowed.
```

Searchable path whitelist (file type):

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

Searchable path whitelist (directory prefix type):

```bash
/sf/cfg/if.d/    (e.g. /sf/cfg/if.d/<*>
/sys/class/net/  (e.g. /sys/class/net/<*>
/sf/log/         (e.g. /sf/log/<*>
/var/log/        (e.g. /var/log/<*>
```

### Usage Example

```bash
acli system grep -n "eth0" /proc/interrupts
```

### Output Example

```bash
58: 30:      0      0      0      0    6452280   eth0-0
89: 63:      0      0      0      0    8388608   eth0.1-0
```
