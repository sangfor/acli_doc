---
sidebar_position: 1
---

# get

### Overview

View interface MTU

### Command Parameters
```bash
-n|--nic-name=string    Required parameter, Port name, example: eth1
```

### Usage Example

```bash
acli network nic mtu get --nic-name eth0
```

### Output Example

```bash
eth0
   mtu: 1500
```