---
sidebar_position: 3
---

# clear

### Overview

Clear the custom NUMA binding of a virtual machine and return to smart NUMA scheduling (effective after restart)

### Command Parameters

```bash
-v|--vm-id=string     Required parameter, VM ID, example: 4872898137715
```

### Usage Example

```bash
# Clear the custom NUMA binding of a VM
acli vm numa clear -v 4872898137715
```

### Output Example

```bash
code: 0
message: success
```
