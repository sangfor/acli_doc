---
sidebar_position: 1
---

# nc

### Overview

Probe connectivity to a host and port and display information returned by the target service.

### Command Parameters

Command format:

```bash
acli system nc [-w seconds] [-i seconds] <host> <port>
```

Supported parameters:

This command uses a closed probe option allowlist. Only the value-taking short options `-w` and `-i` are permitted; unlisted options are rejected.

```text
-w <seconds>  Specify the wait time; the value must be numeric
-i <seconds>  Specify the interval; the value must be numeric
<host>        Required target host; must satisfy the permitted character set
<port>        Required target port, range: 1-65535
```

Exactly two positional arguments, `<host> <port>`, are required. Extra positional arguments are rejected.

The device uses BusyBox nc, without standalone `-z` or `-v` options. The wrapper connects standard input to `/dev/null` and, when `-w` is specified, sets a fallback timeout of the `-w` value plus two seconds. This limits the invocation to a probe: it exits after connecting and reports connectivity, timeout, or failure based on the exit code.

Forbidden arguments:

```text
-l    Listen mode
-e    Execute a program
-f    Read a file (supported by some nc implementations)
-p    Specify a local port
```

All other short options (including `-z` and `-v`) and all long options are rejected. Rejected calls return a human-readable reason and a nonzero exit code without exposing sensitive paths or internal implementation details.

### Usage Example

```bash
acli system nc -w 3 127.0.0.1 22
```

### Output Example

```text
SSH-2.0-OpenSSH_SangforOS
```
