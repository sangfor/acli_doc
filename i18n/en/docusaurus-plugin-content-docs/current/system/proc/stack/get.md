---
sidebar_position: 1
---

# get

### Overview

Get the stack info of the process

### Command Parameters
```bash
-p|--pid=integer            Required parameter, Process ID, example: 122063
```

### Usage Example

```bash
acli system proc stack get -p 105667
```

### Output Example

```bash
[] hrtimer_nanosleep+0xbe/0x1c0
[] __x64_sys_nanosleep+0x6d/0x80
[] do_syscall_64+0x5b/0x1d0
[] entry_SYSCALL_64_after_hwframe+0x65/0xca
```