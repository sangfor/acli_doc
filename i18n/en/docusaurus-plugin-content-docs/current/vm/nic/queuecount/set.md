---
sidebar_position: 1
---

# set

### Overview

Update the number of VM NIC queues

### Command Parameters
```bash
-i|--id=string              Required parameter, NIC ID, Example: 4872898137715:net0
-c|--count=integer          Required parameter, Number of NIC queues, Example: 1
```

### Usage Example

```bash
acli vm nic queuecount set -i 1836960663822:net0 -c 1
```

### Output Example

```bash
taskID: host-005056b2894b:280998:1760441353:6913569233831
message: null
targetID: 1836960663822:net0
```