---
sidebar_position: 1
---

# pstack

### Overview

Read the call stack of a specified process for troubleshooting.

### Command Parameters

Command format:

```bash
acli system pstack [-n depth] <pid>
acli system pstack -h
acli system pstack --help
```

Supported parameters:

This command uses a closed argument allowlist. Unlisted options and arguments are rejected. No write options are permitted.

```text
<pid>        Process ID to query; digits only, at most one positional argument
-n <depth>   Specify the stack depth
-h|--help    Print help information
```

Forbidden arguments:

Only `-n` is permitted for stack depth; there is no corresponding double-dash long option. Other options, nonnumeric PIDs, and extra positional arguments are rejected.

### Usage Example

```bash
acli system pstack 156350
```

Replace the process ID with the actual PID to inspect.

### Output Example

Querying a process call stack:

```text
#0  0x00007f150d6572f0 in nanosleep () from /lib/x86_64-linux-gnu/libc.so.6
#1  0x00007f150d65725a in sleep () from /lib/x86_64-linux-gnu/libc.so.6
#2  0x00007f150e1823b2 in Perl_pp_sleep () from /usr/lib/libperl.so.5.14
#3  0x00007f150e12ec26 in Perl_runops_standard () from /usr/lib/libperl.so.5.14
#4  0x00007f150e0d0755 in perl_run () from /usr/lib/libperl.so.5.14
#5  0x0000000000400f89 in main ()
```

When no PID is specified:

```text
Usage: pstack <process-id>
```
