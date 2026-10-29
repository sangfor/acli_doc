---
sidebar_position: 1
---

# dpping

### Overview

Run ping through the SDN dataplane to check connectivity to a destination.

### Command Parameters

Command format:

```bash
acli network dpping [-c count] [-i interval] [-w deadline] [-s packetsize] [-M hint] [hop1 ...] destination
```

The following arguments correspond to the usage shown in the tool's help:

```text
destination       Required parameter, the destination address
-c count          Specify the number of probe packets to send
-i interval       Specify the interval between probe packets
-w deadline       Specify the deadline for probing
-s packetsize     Specify the probe packet size
-M hint           Specify the path MTU discovery strategy
[hop1 ...]        Optional intermediate hops
```

### Usage Example

```bash
acli network dpping
```

### Output Example

When no destination is specified, the following usage is returned. `ping` is the name shown in the tool's help:

```text
dp ping: support ping with sdn dataplane
Usage: ping [-c count] [-i interval] [-w deadline] [-s packetsize]
            [-M mtu discovery hint] [hop1 ...] destination
```
