---
sidebar_position: 2
---

# fix

### Overview

Fix memory consistency, modify DB and CFS config based on the specified memory size (Dangerous operation: will overwrite existing configuration)

### Command Parameters

```bash
-v|--vm-id=string         Required parameter, VM ID. Example: 614182240912
-m|--memory-mb=integer    Required parameter, force specify memory size in MB. Example: 2048
```

### Usage Example

```bash
# Fix memory consistency
acli vm memory consistency fix -v 614182240912 -m 2048
```

### Output Example

```bash
Are you sure you want to execute the operation? (y[es]/n[o]): y
{"VMID":"614182240912","MemoryMBBefore":4096,"MemoryMBAfter":2048}
```