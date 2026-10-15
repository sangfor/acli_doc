---
sidebar_position: 1
---

# query

### Overview

Query the NUMA binding position of a virtual machine (supports single VM and running VMs on a host)

### Command Parameters

```bash
-v|--vm-id=string     Optional parameter, VM ID (mutually exclusive with --host), example: 4872898137715
-H|--host-id=string   Optional parameter, host ID (mutually exclusive with --vm), returns only running VMs, example: host-0050568eecc7
```

### Usage Example

```bash
# Query the NUMA binding position of a single VM
acli vm numa query -v 4872898137715

# Query the NUMA binding position of all running VMs on a host
acli vm numa query -H host-0050568eecc7
```

### Output Example

```bash
vmID: 4872898137715
name: test-vm
vcpuCount: 8
numaEnabled: true
numaNodes:
  0
  1
runningNumaNodes:
  0
bindStatus: user
```
