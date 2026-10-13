---
sidebar_position: 1
---

# traceroute

### Overview

Trace the network path of packets to a destination host (read-only).

### Command Parameters

No parameters

### Usage Example

```bash
acli system traceroute -n 8.8.8.8
```

### Output Example

```bash
# acli system traceroute -n 8.8.8.8
traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets
 1  10.0.0.1  0.324 ms  0.289 ms  0.312 ms
 2  192.168.1.1  1.025 ms  0.998 ms  1.112 ms
 3  8.8.8.8  10.231 ms  10.198 ms  10.245 ms
```
