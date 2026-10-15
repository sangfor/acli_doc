---
sidebar_position: 5
---

# batch-clear

### Overview

Batch clear the custom NUMA binding of virtual machines and return to smart NUMA scheduling (processed per VM, partial success and failures listed with reasons, effective after restart)

### Command Parameters

```bash
-v|--vm-ids=array     Required parameter, list of VM IDs, example: --vm-ids.1 7369491980128 --vm-ids.2 7291549938786
--vm-ids.N=string    Each element in the vm-ids parameter, example: 7291549938786
```

### Usage Example

```bash
# Batch clear the custom NUMA binding of two VMs
acli vm numa batch-clear --vm-ids.1 7369491980128 --vm-ids.2 7291549938786
```

### Output Example

```bash
code: 0
message: success
```
