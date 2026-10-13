---
sidebar_position: 1
---

# set

### Overview

Generate FCoE configuration for the specified NIC and restart related services

### Command Parameters

```bash
-i|--interface=string    Required parameter, NIC name, Example: eth7
```

### Usage Example

```bash
acli network nic fcoe set --interface eth7
```

### Output Example

```bash
Setting successful, FCoE interface configuration has been generated and applied
```