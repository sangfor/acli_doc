---
sidebar_position: 1
---

# disable

### Overview

Disable access to the VM console

### Command Parameters
```bash
-v|--vm-ids=array           Required parameter, VM ID list, Example: --vm-ids.1 7369491980128 --vm-ids.2 7291549938786
--vm-ids.N=string           Each element in the vm-ids parameter, Element example: 7291549938786
```

### Usage Example

```bash
acli vm vnc disable --vm-ids.1 7369491980128 --vm-ids.2 7291549938786
```

### Output Example

```bash
# Success
code: 0
message:
# Failed
code: 500
message: "Failed to update VNC configuration."
```