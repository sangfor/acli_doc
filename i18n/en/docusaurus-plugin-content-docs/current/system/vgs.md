---
sidebar_position: 1
---

# vgs

### Overview

Display LVM volume group information.

### Command Parameters

Command format:

```bash
acli system vgs [options] [VG|Tag ...]
```

`VG|Tag ...` optionally specifies volume groups or tags. If omitted, the command lists volume groups.

The help output below describes tool options for display fields, selection, sorting, and report formats.

### Usage Example

```bash
acli system vgs -h
```

### Output Example

Running `acli system vgs -h` returns the following help:

```text
  vgs - Display information about volume groups

  vgs
        [ -a|--all ]
        [ -o|--options String ]
        [ -S|--select String ]
        [ -O|--sort String ]
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
        [ VG|Tag ... ]

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
