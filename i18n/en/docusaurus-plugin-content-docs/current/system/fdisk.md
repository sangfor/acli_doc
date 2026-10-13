---
sidebar_position: 1
---

# fdisk

### Overview

View disk partition information (read-only).

### Command Parameters

This is a partially read-only command using a closed parameter whitelist (only listed parameters are allowed, others are rejected).

```bash
-l|--list=flag  Optional parameter. List the partition information of a specified device (only whitelisted paths are allowed). Example: acli system fdisk -l /dev/sda
```

Path whitelist (dev command family path whitelist; only 1 entry, the /dev/ directory):

```bash
/dev/  (block device directory, prefix match, e.g. /dev/sda)
```

Write parameters (rejected on match):

```bash
Entering the interactive partition menu without -l (can write to disk)  Interactive partition menu, can write to disk
n/d/w/t/a/m/p (interactive commands)                                    Interactive commands: new/delete/write/type/toggle/menu/print
```

### Usage Example

```bash
acli system fdisk -l /dev/sda
```

### Output Example

```bash
# acli system fdisk -l /dev/sda
Disk /dev/sda: 1.8 TiB, 2000398934016 bytes, 3907029168 sectors
Disk model: SATA SSD
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: gpt
Disk identifier: 12345678-90AB-CDEF-1234-567890ABCDEF

Device       Start        End    Sectors   Size Type
/dev/sda1     2048    2099199    2097152     1G EFI System
/dev/sda2  2099200  3907028991 3904929792   1.8T Linux filesystem
```
