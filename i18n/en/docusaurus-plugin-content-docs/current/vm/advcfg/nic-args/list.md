---
sidebar_position: 1
---

# list

### Overview

List all NICs and their custom QEMU args of the VM

### Command Parameters

```bash
-v|--vm-id=string    Required parameter, virtual machine ID, example: 6520699837375
```

### Usage Example

```bash
acli vm advcfg nic-args list -v 6520699837375
```

### Output Example

```bash
nics:
  [0]:
    customArgs:
    index: 0
    nicID: f89a68a0-e44f-494b-9c52-7c47100cfddd
    nicName: net0
  [1]:
    customArgs:
    index: 1
    nicID: 3e35de83-cb2e-4ef8-80ad-c4c41ad550e3
    nicName: net1
vmID: 6520699837375
```