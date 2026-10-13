---
sidebar_position: 1
---

# delete

### Overview

Delete FCoE configuration for the specified NIC and restart related services

### Command Parameters

```bash
-i|--interface=string    Required parameter, NIC name, Example: eth7
```

### Usage Example

```bash
acli network nic fcoe delete --interface eth7
```

### Output Example

```bash
FCoE interface configuration has been deleted
```