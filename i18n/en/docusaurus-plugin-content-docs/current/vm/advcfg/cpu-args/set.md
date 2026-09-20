---
sidebar_position: 1
---

# set

### Overview

Modify the custom QEMU args of the VM CPU (cold edit, only supported when the VM is powered off; not supported on ARM, an error is returned)

### Command Parameters

```bash
-v|--vm-id=string    Required parameter, virtual machine ID, example: 6520699837375
-V|--value=string    Required parameter, CPU custom QEMU args string (plain comma-separated), example: hv_vendor_id=CustomOEM. Overwrite semantics: a value replaces it, an empty string clears it
```

### Usage Example

```bash
acli vm advcfg cpu-args set -v 6520699837375 -V hv_vendor_id=CustomOEM
```

### Output Example

```bash
Are you sure you want to execute the operation? (y[es]/n[o]): y
customArgsAfter: hv_vendor_id=CustomOEM
customArgsBefore:
vmID: 6520699837375
```

Rejected while the VM is running:

```bash
Error: the VM is running, please power it off before modifying the custom QEMU args!
```