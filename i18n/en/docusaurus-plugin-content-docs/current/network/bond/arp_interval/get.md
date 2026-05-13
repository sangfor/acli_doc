---
sidebar_position: 1
---

# get

### Overview

Obtain the ARP liveness probing frequency of aggregate interface

### Command Parameters
```bash
-b|--bond-name=string    Required parameter, Aggregate interface name, Example: sf_vs_bond0
```

### Usage Example

```bash
acli network bond arp_interval get -b bond0
```

### Output Example

```bash
2000
```