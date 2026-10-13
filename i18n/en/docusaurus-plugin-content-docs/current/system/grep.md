---
sidebar_position: 1
---

# grep

### Overview

Search for matching lines by keyword in configuration or system files that are whitelisted.

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

Searchable path whitelist (shared by the cat command family: cat/grep/tail/diff text-view/compare family; 81 entries after redundancy removal; excerpt):

File type (exact match, excerpt):

```bash
/cfs/.members
/cfs/cfgmaster.ini
/cfs/cluster.ini
/cfs/storage.cfg
/etc/fstab
/etc/hosts
/etc/issue
/etc/machine-id
/etc/resolv.conf
/sf/version
/sf/vs/version
/sys/class/dmi/id/sys_vendor
/root/.bash_history
/var/log/sfvt_p2vagt.log
```

Directory prefix type (prefix match, excerpt):

```bash
/proc/                 (e.g. /proc/cpuinfo, /proc/meminfo, /proc/interrupts)
/etc/sysconfig/        (e.g. /etc/sysconfig/<*>)
/sys/class/net/        (e.g. /sys/class/net/<*>)
/sys/bus/pci/devices/  (e.g. /sys/bus/pci/devices/<*>)
/sf/log/               (e.g. /sf/log/<*>)
/var/log/              (e.g. /var/log/<*>)
/tmp/                  (e.g. /tmp/<*>)
```

Wildcard type (glob match, excerpt):

```bash
/etc/lvm/archive/*.vg
/sf/cfg/vs/disk/*
/sys/devices/system/edac/mc/mc*/csrow*/ch*
/boot/grub2/grub.cfg*
```

### Usage Example

```bash
acli system grep -n "eth0" /proc/interrupts
```

### Output Example

```bash
# acli system grep -n "eth0" /proc/interrupts
 30:      0      0      0      0    6452280   eth0-0
 63:      0      0      0      0    8388608   eth0.1-0
```
