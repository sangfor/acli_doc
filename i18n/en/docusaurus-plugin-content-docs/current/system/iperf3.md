---
sidebar_position: 1
---

# iperf3

### Overview

Network bandwidth measurement diagnostic tool for TCP/UDP throughput testing (read-only, does not change system state). The command runs inside the vs-cp-manager container (which shares the network namespace with the vs container).

### Command Parameters

This is a partially read-only command; options are not whitelisted (allowed by default), but the blacklisted parameters below are rejected on match.

Forbidden parameters (rejected on match, including GNU unique-prefix abbreviations):

```bash
--logfile=<file>  Writes logs to a file (write operation). Rejected. Because GNU getopt accepts
                  unique-prefix abbreviations, any form starting with --lo (--lo / --log) is also
                  rejected. Note that --length is unaffected (its shortest unique prefix is --le).
```

### Usage Example

```bash
acli system iperf3 -c 127.0.0.1 -p 5201 -t 5
```

### Output Example

```bash
# acli system iperf3 -c 127.0.0.1 -p 5201 -t 5
Connecting to host 127.0.0.1, port 5201
[  4] local 127.0.0.1 port 51234 connected to 127.0.0.1 port 5201
[ ID] Interval           Transfer     Bitrate
[  4]   0.00-5.00  sec   1.10 GBytes  1.89 Gbits/sec                  sender
[  4]   0.00-5.00  sec   1.10 GBytes  1.89 Gbits/sec                  receiver

iperf Done.
```