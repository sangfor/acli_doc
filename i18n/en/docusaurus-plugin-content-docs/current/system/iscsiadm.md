---
sidebar_position: 1
---

# iscsiadm

### Overview

Query iSCSI sessions, discover targets, and display node information using the permitted read-only argument combinations.

### Command Parameters

Command format:

```bash
acli system iscsiadm -m session
acli system iscsiadm -m discovery -t st -p <IP:Port>
acli system iscsiadm -m discovery -t sendtargets -p <IP:Port>
acli system iscsiadm -m node
acli system iscsiadm -m node -o show
```

Supported parameters:

This command uses a closed argument allowlist. Only the following POSIX short-option combinations are permitted; unlisted options and write operations are rejected.

```text
-m session      Query current iSCSI sessions
-m discovery    Discover iSCSI targets; requires -t and -p
-t st           SendTargets discovery type (sendtargets is also supported)
-p <IP:Port>    Specify the target portal IP address and port
-m node         Query iSCSI node information
-o show         Display node information; the only permitted node operation
```

Forbidden arguments:

```text
-o new
-o delete
-o update
-m iface -o update
```

The iface mode and all other unlisted combinations are also rejected. An option appearing in an allowed combination does not make it independently permitted.

### Usage Example

```bash
acli system iscsiadm -m session
```

### Output Example

```text
iscsiadm: No active sessions.
```
