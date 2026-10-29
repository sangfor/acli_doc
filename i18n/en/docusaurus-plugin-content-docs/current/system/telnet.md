---
sidebar_position: 1
---

# telnet

### Overview

Probe connectivity to a specified host and port. Only the read-only port probing form is permitted.

### Command Parameters

Command format:

```bash
acli system telnet <host> <port>
acli system telnet -h
acli system telnet --help
```

Supported parameters:

This command uses a closed argument allowlist. Unlisted arguments are rejected.

```text
<host>      Required target host; must satisfy the permitted character set
<port>      Required target port, range: 1-65535
-h|--help   Only permitted as the sole argument; print help information
```

Forbidden arguments:

A probe must contain exactly two positional arguments, `<host> <port>`. Except for `-h` or `--help` used alone, all options beginning with `-` are rejected. Extra arguments, interactive login, and write operations are not permitted.

### Usage Example

```bash
acli system telnet 127.0.0.1 22
```

### Output Example

```text
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
Connection closed by foreign host.
```
