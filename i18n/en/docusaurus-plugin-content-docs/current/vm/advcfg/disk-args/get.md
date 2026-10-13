---
sidebar_position: 1
---

# get

### Overview

Query the custom QEMU args of the specified disk of the VM

### Command Parameters

```bash
-v|--vm-id=string      Required parameter, virtual machine ID, example: 6520699837375
-d|--disk-id=string    Required parameter, disk ID (UUID), example: 01a0b267-4842-7f0b-8e18-864986d2e3da (can be obtained via 'vm advcfg disk-args list')
```

### Usage Example

```bash
acli vm advcfg disk-args get -v 6520699837375 -d 01a0b267-4842-7f0b-8e18-864986d2e3da
```

### Output Example

When not set:

```bash
deviceArgs:
diskID: 01a0b267-4842-7f0b-8e18-864986d2e3da
diskName: opencloud-disk-0-20260918
driveArgs:
slot: ide0
vmID: 6520699837375
```

When set:

```bash
deviceArgs: serial=SN-001
diskID: 01a0b267-4842-7f0b-8e18-864986d2e3da
diskName: opencloud-disk-0-20260918
driveArgs: iothread=iothread0,copy-on-read=on
slot: ide0
vmID: 6520699837375
```