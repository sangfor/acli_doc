---
sidebar_position: 1
---

# switch

### Overview

Switch management interface role to the specified interface

### Command Parameters
```bash
-i|--iface=string        Required parameter, New management interface name, Example: eth2
-c|--carry-ip=integer    Whether to switch the existing management interface IP to the specified interface, The IP address is switched by default. Example: 0 (without IP), 1 (with IP), Enum values: 0,1
```

### Usage Example

```bash
acli network mgmt switch -i eth3

acli network mgmt switch -i eth4 -c 0
```

### Output Example

```bash
UPID: host-0050568e2936:0000A6D9:655C:69B27910:Edit Management Port:3:admin@vtp:
```