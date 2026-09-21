---
sidebar_position: 1
---

# uniq

### Overview

Filter and output adjacent duplicate lines from a file or input stream; piped input is supported (read-only).

### Command Parameters

This is a fully read-only command; options are all allowed (no option whitelist). At most 1 positional argument is accepted, and its path must be in the shared path whitelist of the cat command family.

```bash
<file>  Optional parameter. The file to filter; at most 1. Path must be in the cat family path whitelist. Example: /var/log/messages
-c      Optional parameter. Prefix each line with the number of occurrences. Example: acli system uniq -c /var/log/messages
-d      Optional parameter. Only print duplicate lines
-u      Optional parameter. Only print unique lines
-i      Optional parameter. Ignore case when comparing
-f <N>  Optional parameter. Skip the first N fields on each line
-s <N>  Optional parameter. Skip the first N characters on each line
-w <N>  Optional parameter. Compare at most the first N characters on each line
```

If `<file>` is omitted, input is read from stdin, so the command can be used with pipes.

Filterable path whitelist (shared by the cat command family: cat/grep/tail/diff text-view/compare family; 81 entries after redundancy removal; excerpt):

File entries (exact match, excerpt):

```bash
/cfs/.members
/cfs/cfgmaster.ini
/etc/fstab
/etc/hosts
/etc/machine-id
/etc/resolv.conf
/sf/version
```

Directory-prefix entries (prefix match, excerpt):

```bash
/proc/
/sys/class/net/
/sf/log/
/var/log/
/tmp/
```

Glob entries (glob match, excerpt):

```bash
/etc/lvm/archive/*.vg
/sf/cfg/vs/disk/*
/boot/grub2/grub.cfg*
```

### Usage Example

```bash
acli system uniq /var/log/messages
```

```bash
acli system uniq -c /var/log/messages
```

### Output Example

```bash
# acli system uniq /var/log/messages
line a
line b
line c
```