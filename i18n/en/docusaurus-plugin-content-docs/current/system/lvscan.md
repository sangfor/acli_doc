---
sidebar_position: 1
---

# lvscan

### Overview

List all logical volumes in all volume groups.

### Command Parameters

Command format:

```bash
acli system lvscan [options]
```

The help output below describes tool options for listing all logical volumes, block device information, and report formats.

### Usage Example

```bash
acli system lvscan -h
```

### Output Example

Running `acli system lvscan -h` returns the following help:

```text
  lvscan - List all logical volumes in all volume groups

  lvscan
        [ -a|--all ]
        [ -b|--blockdevice ]
        [    --ignorelockingfailure ]
        [    --readonly ]
        [    --reportformat basic|json|json_std ]
        [ COMMON_OPTIONS ]

  Common options for lvm:
        [ -d|--debug ]
        [ -h|--help ]
        [ -q|--quiet ]
        [ -v|--verbose ]
        [ -y|--yes ]
        [ -t|--test ]
        [    --commandprofile String ]
        [    --config String ]
        [    --driverloaded y|n ]
        [    --nolocking ]
        [    --lockopt String ]
        [    --longhelp ]
        [    --profile String ]
        [    --version ]
        [    --devicesfile String ]
        [    --devices PV ]
        [    --nohints ]
        [    --journal String ]

  Use --longhelp to show all options and advanced commands.
```
