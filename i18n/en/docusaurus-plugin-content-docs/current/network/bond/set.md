---
sidebar_position: 1
---

# set

### Overview

Update aggregate interface

### Command Parameters
```bash
-h|--hostname=string     Node ID, Example: host-005056b2a30a, Default: enable_hostname_cmd
-b|--bond-name=string    Required parameter, Aggregate interface name, Example: channel1
-m|--members=string      Member interface name, Separate multiple names with commas. Example: eth2,eth3
-d|--mode=string         Aggregate interface modes: active-backup (static aggregation with active/standby (mode: 1)), layer2 (static aggregation with MAC-based load balancing (mode: 2)), layer23 (static aggregation with IP-based load balancing (mode: 2)), balance-rr (static aggregation with round robin among interfaces (mode: 0)), layer34 (static aggregation with Layer 4-based load balancing (mode: 2)), lacp-layer2 (LACP mode with MAC-based load balancing (mode: 4)), lacp-layer23 (LACP mode with IP-based load balancing (mode: 4)), lacp-layer34 (LACP mode with Layer 4-based load balancing (mode: 4)),, Enum values: active-backup,layer2,layer23,balance-rr,layer34,lacp-layer2,lacp-layer23,lacp-layer34
```

### Usage Example

```bash
acli network bond set --hostname host-005056b2ec8d --bond-name channel1 --members eth2,eth3 --mode layer23
```

### Output Example

```bash
task_id: UPID:host-005056b2ec8d:00009AFB:1ADD4A0:6875BA28:Edit Network Port:16:admin@vtp:
```