---
sidebar_position: 1
---

# get

### Overview

View the networking mode of aggregate interface

### Command Parameters
```bash
-b|--bond-name=string    Required parameter, Aggregate interface name, Example: sf_vs_bond0
```

### Usage Example

```bash
acli network bond mode get -b bond0
```

### Output Example

```bash
balance-rr 0
```