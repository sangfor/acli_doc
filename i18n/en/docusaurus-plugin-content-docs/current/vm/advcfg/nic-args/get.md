---
sidebar_position: 1
---

# get

### Overview

Query the custom QEMU args of the specified NIC of the VM

### Command Parameters

```bash
-v|--vm-id=string     Required parameter, virtual machine ID, example: 6520699837375
-n|--nic-id=string    Required parameter, NIC ID (iface_id), example: f89a68a0-e44f-494b-9c52-7c47100cfddd (can be obtained via 'vm advcfg nic-args list')
```

### Usage Example

```bash
acli vm advcfg nic-args get -v 6520699837375 -n f89a68a0-e44f-494b-9c52-7c47100cfddd
```

### Output Example

When not set:

```bash
customArgs:
index: 0
nicID: f89a68a0-e44f-494b-9c52-7c47100cfddd
nicName: net0
vmID: 6520699837375
```

When set:

```bash
customArgs: mq=on,vectors=8
index: 0
nicID: f89a68a0-e44f-494b-9c52-7c47100cfddd
nicName: net0
vmID: 6520699837375
```