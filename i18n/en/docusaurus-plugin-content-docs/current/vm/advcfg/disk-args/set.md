---
sidebar_position: 1
---

# set

### Overview

Modify the custom QEMU args of the VM disk (cold edit, only supported when the VM is powered off)

### Command Parameters

```bash
-v|--vm-id=string         Required parameter, virtual machine ID, example: 6520699837375
-t|--type=string          Required parameter, scope, enum values: vm (modify all disks of the VM), disk (modify only the single disk specified by --disk-id), case-insensitive, example: disk. Only supported when the VM is powered off
-d|--disk-id=string       Optional parameter, disk ID (UUID), example: 01a0b267-4842-7f0b-8e18-864986d2e3da. Required when --type disk; ignored when --type vm
-D|--drive-args=string    Optional parameter, custom qemu -drive tail args (plain comma-separated), example: iothread=iothread0,copy-on-read=on. Overwrite semantics: a value replaces the field, an empty string clears it, and omitting it leaves the field unchanged. Note: for values starting with -, use the = form; values must not contain high-risk Linux command words, otherwise they are blocked by the security filter
-a|--device-args=string   Optional parameter, custom qemu -device tail args (plain comma-separated), example: serial=SN-001. Overwrite semantics: a value replaces the field, an empty string clears it, and omitting it leaves the field unchanged. Note: for values starting with -, use the = form; values must not contain high-risk Linux command words, otherwise they are blocked by the security filter
```

### Usage Example

```bash
# Modify a single disk
acli vm advcfg disk-args set -v 6520699837375 -t disk -d 01a0b267-4842-7f0b-8e18-864986d2e3da -D "iothread=iothread0,copy-on-read=on" -a "serial=SN-001"
# Modify all disks (only the -drive args)
acli vm advcfg disk-args set -v 6520699837375 -t vm -D "iothread=iothread0"
```

### Output Example

Modify a single disk (`--type disk`):

```bash
Are you sure you want to execute the operation? (y[es]/n[o]): y
diskID: 01a0b267-4842-7f0b-8e18-864986d2e3da
diskIDs:
  [0]: 01a0b267-4842-7f0b-8e18-864986d2e3da
perDiskChanges:
  [0]:
    deviceArgsAfter: serial=SN-001
    deviceArgsBefore:
    diskID: 01a0b267-4842-7f0b-8e18-864986d2e3da
    driveArgsAfter: iothread=iothread0,copy-on-read=on
    driveArgsBefore:
    slot: ide0
scope: disk
vmID: 6520699837375
```

Modify all disks (`--type vm`):

```bash
Are you sure you want to execute the operation? (y[es]/n[o]): y
diskIDs:
  [0]: 01a0b267-4842-7f0b-8e18-864986d2e3da
perDiskChanges:
  [0]:
    deviceArgsAfter:
    deviceArgsBefore:
    diskID: 01a0b267-4842-7f0b-8e18-864986d2e3da
    driveArgsAfter: iothread=iothread0
    driveArgsBefore:
    slot: ide0
scope: vm
vmID: 6520699837375
```