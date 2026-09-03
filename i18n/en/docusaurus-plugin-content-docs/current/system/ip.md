---
sidebar_position: 1
---

# ip

### Overview

View node network information, which supports read-only queries of address, route, link, and neighbor information.

### Command Parameters

```bash
addr show   View node address information (alias a is also available).
route show  View route information
link show   View link information
neigh show  View neighbor information
```

### Usage Example

```bash
acli system ip route show
```

### Output Example

```bash
default via 10.131.136.1 dev eth0
10.131.136.0/24 dev eth0 proto kernel scope link src 10.131.136.168
172.18.0.0/16 dev docker0 proto kernel scope link src 172.18.0.1
```
