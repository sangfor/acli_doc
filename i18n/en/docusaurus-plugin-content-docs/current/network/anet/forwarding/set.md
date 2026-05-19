---
sidebar_position: 1
---

# set

### Overview

Adjust forwarding core

### Command Parameters
```bash
-h|--high-performance=integer       Is the forwarding core exclusive, 0(off), 1(on), Enum values: 0,1
-c|--forward-cores=integer          Forwarding core quantity, for example: 8
-s|--supthcore-exclusive=integer    Whether to enable hyper-threading core exclusivity, 0 (disable), 1 (enable), Enum values: 0,1
-v|--vm-queue-batch-size=integer    VM Queues per Batch, enumeration values: [0, 8, 16, 32, 64, 128, 256], Enum values: 0,8,16,32,64,128,256
```

### Usage Example

```bash
acli network anet forwarding set --high-performance 1 --supthcore-exclusive 1 --vm-queue-batch-size 16
```

### Output Example

```bash
forwardCores: 1
highPerformance: true
supthcoreExclusive: true
vmQueueBatchSize: 16
```