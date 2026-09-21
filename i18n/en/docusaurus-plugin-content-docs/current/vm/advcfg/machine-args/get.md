---
sidebar_position: 1
---

# get

### Overview

Query the custom QEMU args of the VM machine

### Command Parameters

```bash
-v|--vm-id=string    Required parameter, virtual machine ID, example: 6520699837375
```

### Usage Example

```bash
acli vm advcfg machine-args get -v 6520699837375
```

### Output Example

When not set:

```bash
args:
vmID: 6520699837375
```

When set:

```bash
args: -no-hpet -nodefaults
vmID: 6520699837375
```