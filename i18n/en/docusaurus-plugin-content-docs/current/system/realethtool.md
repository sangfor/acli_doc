---
sidebar_position: 1
---

# realethtool

### Overview

Query NIC status, statistics, driver details, and related diagnostic information.

### Command Parameters

Command format:

```bash
acli system realethtool [-S|-i|-a|-g|-m|-t] DEVNAME
```

Supported parameters:

This command uses a closed option allowlist. Only the listed options are permitted; other options are rejected.

```bash
-S|--statistics=flag  View NIC statistics
-i|--driver=flag      View driver information of NIC
-a|--all=flag         View all NIC information
-g|--show-ring=flag   View NIC ring buffer parameters
-m|--show-module=flag View module information
-t=flag               Run NIC self-tests
--show-priv-flags     View NIC private flags
-h|--help=flag        Show help information
DEVNAME               Required NIC name (must be an allowlisted interface), for example: eth0
```

Forbidden arguments:

Options outside this allowlist are rejected, including options that modify NIC configuration.

### Usage Example

```bash
acli system realethtool -g eth0
```

### Output Example

```bash
# acli system realethtool -g eth0
Ring parameters for eth0:
Pre-set maximums:
RX:             4096
RX Mini:        2048
RX Jumbo:       4096
TX:             4096
Current hardware settings:
RX:             1024
RX Mini:        128
RX Jumbo:       512
TX:             512
```
