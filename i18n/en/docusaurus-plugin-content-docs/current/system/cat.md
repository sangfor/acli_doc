---
sidebar_position: 1
---

# cat

### Overview

Read and view contents of specified files in the system whitelist.

### Command Parameters

```bash
<file>  Required parameter: specify the path of the file to read. Only paths in the whitelist can be viewed. Example: /etc/hosts
```

Viewable path whitelist (shared by the cat command family: cat/grep/tail/diff text-view/compare family; 81 entries after redundancy removal; excerpt):

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
acli system cat /etc/hosts
```

### Output Example

```bash
# acli system cat /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
```
