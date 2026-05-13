---
sidebar_position: 1
---

# reorder

### Overview

Adjust interface order

### Command Parameters
```bash
-b|--before=string    Required parameter, Interface list before adjustment, Example: eth0 eth1 eth2
-a|--after=string     Required parameter, Interface list after adjustment, Example: eth2 eth1 eth0
```

### Usage Example

```bash
acli network nic reorder --before "eth0 eth1 eth2 eth3 eth4 eth5" --after "eth0 eth1 eth2 eth3 eth4 eth5"
```

### Output Example

```bash

```
```