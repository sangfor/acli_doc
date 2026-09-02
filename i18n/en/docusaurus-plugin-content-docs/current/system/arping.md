---
sidebar_position: 1
---

# arping

### Overview

Send an ARP request to the specified node to detect its online status.

### Command Parameters

```bash
-c|--count=integer     Specify the number of requests sent, for example: 5
-i|--interface=string  Specify NIC interface used for connection, e.g., eth0.
-s|--source=string     Specify source IP address.
<ip>                   Mandatory parameter specifying the target IP address for detection. Example: 10.10.1.2
```

### Usage Example

```bash
acli system arping -i eth0 -c 5 10.10.1.2
```

### Output Example

```bash
ARPING 10.10.1.2 from 10.131.136.168 eth0
Unicast reply from 10.10.1.2 [00:0C:29:56:B7:A6]  1.342ms
Unicast reply from 10.10.1.2 [00:0C:29:56:B7:A6]  1.101ms
Unicast reply from 10.10.1.2 [00:0C:29:56:B7:A6]  1.252ms
Sent 3 probes (1 broadcast(s))
Received 3 response(s)
```
