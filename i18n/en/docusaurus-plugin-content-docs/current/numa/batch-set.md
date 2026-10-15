---
sidebar_position: 4
---

# batch-set

### Overview

Batch set the specified NUMA binding position of virtual machines (validated per VM, partial success and failures listed with reasons, effective after restart)

### Command Parameters

```bash
-v|--vm-ids=array     Required parameter, list of VM IDs, example: --vm-ids.1 7369491980128 --vm-ids.2 7291549938786
--vm-ids.N=string    Each element in the vm-ids parameter, example: 7291549938786
-n|--nodes=array      Required parameter, unified list of NUMA nodes to specify, example: --nodes.1 0 --nodes.2 1
--nodes.N=integer    Each element in the nodes parameter, example: 0
```

### Usage Example

```bash
# Batch bind two VMs to NUMA nodes 0 and 1
acli vm numa batch-set --vm-ids.1 7369491980128 --vm-ids.2 7291549938786 --nodes.1 0 --nodes.2 1
```

### Output Example

```bash
code: 0
message: success
```
