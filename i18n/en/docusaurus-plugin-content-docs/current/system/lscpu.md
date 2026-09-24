---
sidebar_position: 1
---

# lscpu

### Overview

View CPU architecture information (architecture, model, cores, threads, etc., read-only).

### Command Parameters

No parameters

### Usage Example

```bash
acli system lscpu
```

### Output Example

```bash
# acli system lscpu
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                32
On-line CPU(s) list:   0-31
Thread(s) per core:    2
Core(s) per socket:    16
Socket(s):             1
Model name:            Intel(R) Xeon(R) Gold 5220R CPU @ 2.20GHz
```
