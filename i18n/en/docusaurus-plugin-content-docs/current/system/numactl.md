---
sidebar_position: 1
---

# numactl

### Overview

Query NUMA topology and policy

### Command Parameters

```bash
-H|--hardware=flag  Show NUMA hardware topology (default when no parameter is given)
-s|--show=flag      Show current NUMA policy
```

### Usage Example

```bash
acli system numactl --hardware
acli system numactl --show
```

### Output Example

```bash
available: 1 nodes (0)
node 0 cpus: 0 1 2 3 4 5 6 7
node 0 size: 39617 MB
node 0 free: 18712 MB
node distances:
node   0 
  0:  10 
```
