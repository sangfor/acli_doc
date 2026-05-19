---
sidebar_position: 1
---

# set

### Overview

Configure interface MTU

### Command Parameters
```bash
-h|--hostname=string    Node ID, Example: host-005056b2a30a, Default: enable_hostname_cmd
-n|--nic-name=string    Required parameter, Interface name
-m|--mtu=string         Required parameter, Maximum Transmission Unit
```

### Usage Example

```bash
acli network nic mtu set --hostname host-005056b2ec8d --nic-name eth4 --mtu 1600
```

### Output Example

```bash
task_id: UPID:host-005056b2ec8d:00009AFB:1ADD4A0:68774DFC:Edit Network Port:20:admin@vtp:
```