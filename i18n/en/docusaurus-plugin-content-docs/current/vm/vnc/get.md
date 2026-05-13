---
sidebar_position: 1
---

# get

### Overview

Obtain the VM console configuration

### Command Parameters
```bash
-v|--vm-ids=array           Required parameter, VM ID list, Example: --vm-ids.1 7369491980128 --vm-ids.2 7291549938786
--vm-ids.N=string           Each element in the vm-ids parameter, Element example: 7291549938786
```

### Usage Example

```bash
acli vm vnc get --vm-ids.1 7369491980128 --vm-ids.2 7291549938786
```

### Output Example

```bash
data:
  [0]:
    isEnabled: false
    vmid: 7291549938786
  [1]:
    isEnabled: false
    vmid: 7369491980128
message:
```