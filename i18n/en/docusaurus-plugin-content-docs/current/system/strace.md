---
sidebar_position: 1
---

# strace

### Overview

strace command, only supports tracing acli commands

### Command Parameters

No parameters
### Usage Example

```bash
acli system strace
```

### Output Example

```bash
# Trace System Calls of the acli system ps Command
acli system strace acli system ps
execve("/usr/bin/acli", ["acli", "system", "ps"], 0x7ffd12345678 /* 50 vars */) = 0
brk(NULL)                               = 0x555555556000
arch_prctl(0x3001 /* ARCH_??? */, 0x7ffd12345600) = -1 EINVAL (Invalid argument)
...
```