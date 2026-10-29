---
sidebar_position: 1
---

# pvs

### Overview

Display LVM physical volume information.

### Command Parameters

Command format:

```bash
acli system pvs [options] [PV|Tag ...]
```

`PV|Tag ...` optionally specifies physical volumes or tags. If omitted, the command lists physical volumes.

The help output below describes tool options for display fields, selection, sorting, segments, and report formats.

### Usage Example

```bash
acli system pvs -h
```

### Output Example

Running `acli system pvs -h` returns the following help:

```text
  pvs - Display information about physical volumes

  pvs
        [ -a|--all ]
        [ -o|--options String ]
        [ -S|--select String ]
        [ -O|--sort String ]
        [    --segments ]
        [    --aligned ]
        [    --binary ]
        [    --configreport log|vg|lv|pv|pvseg|seg ]
        [    --foreign ]
        [    --ignorelockingfailure ]
        [    --logonly ]
        [    --nameprefixes ]
        [    --noheadings ]
        [    --nosuffix ]
        [    --readonly ]
        [    --reportformat basic|json|json_std ]
        [    --rows ]
        [    --separator String ]
        [    --shared ]
        [    --unbuffered ]
        [    --units [Number]r|R|h|H|b|B|s|S|k|K|m|M|g|G|t|T|p|P|e|E ]
        [    --unquoted ]
        [ COMMON_OPTIONS ]
        [ PV|Tag ... ]

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
