---
sidebar_position: 2
---

# set

### Overview

Set the specified NUMA binding position of a virtual machine (configuration applied, effective after restart)

### Command Parameters

```bash
-v|--vm-id=string     Required parameter, VM ID, example: 4872898137715
-n|--nodes=array      Required parameter, list of NUMA nodes to specify, example: --nodes.1 0 --nodes.2 1
--nodes.N=integer    Each element in the nodes parameter, example: 0
```

### Usage Example

```bash
# Bind the VM to NUMA nodes 0 and 1
acli vm numa set --vm-id 4872898137715 --nodes.1 0 --nodes.2 1
```

### Output Example

```bash
code: 0
message: success
```
