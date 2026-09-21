---
sidebar_position: 1
---

# get

### Overview

Query the custom QEMU args of the VM CPU

### Command Parameters

```bash
-v|--vm-id=string    Required parameter, virtual machine ID, example: 6520699837375
```

### Usage Example

```bash
acli vm advcfg cpu-args get -v 6520699837375
```

### Output Example

When not set:

```bash
customArgs:
vmID: 6520699837375
```

When set:

```bash
customArgs: hv_vendor_id=CustomOEM
vmID: 6520699837375
```