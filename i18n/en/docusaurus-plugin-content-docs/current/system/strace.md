---
sidebar_position: 1
---

# strace

### Overview

strace command, only supports tracing system calls of acli commands (read-only, does not modify
system state).

### Command Parameters

```bash
<command>  Positional argument. The command to trace; only acli is allowed. Example: acli system strace acli system du /tmp
-c         Optional parameter. Count time and calls for each system call. Example: acli system strace -c acli system ps
-f         Optional parameter. Trace child processes. Example: acli system strace -f acli system ps
-e <expr>  Optional parameter. Specify the system call expression to trace. Example: -e trace=openat
-p <pid>   Optional parameter. Trace the given process. Example: -p 1234
-s <size>  Optional parameter. Specify the maximum string length to display. Example: -s 128
```

Forbidden parameters (rejected on match, including GNU unique-prefix abbreviations):

```bash
-o <file>        Forbidden. Writes trace output to a file (write operation). Rejected. Combined
                 forms (-ofile / -fo, etc.) are also rejected.
--output=<file>  Forbidden. Writes trace output to a file. Rejected. Because GNU getopt accepts
                 unique-prefix abbreviations, any form starting with --o (--o / --ou / --out) is
                 also rejected.
<command>        Forbidden. Any first positional argument other than acli is rejected (only
                 tracing acli commands is allowed).
```

### Usage Example

```bash
acli system strace acli system ps
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