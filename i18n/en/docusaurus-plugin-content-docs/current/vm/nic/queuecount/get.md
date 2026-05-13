---
sidebar_position: 1
---

# get

### Overview

Obtain the number of VM NIC queues

### Command Parameters
```bash
-i|--id=string              Required parameter, NIC ID, Example: 4872898137715:net0
```

### Usage Example

```bash
acli vm nic queuecount get --id 1836960663822:net0
```

### Output Example

```bash
numQueues: 1
```