---
sidebar_position: 1
---

# set

### Overview

Configure the number of interface queues

### Command Parameters
```bash
-h|--hostname=string      Node ID, default value, and current node ID, Example: host-005056893c9d, Default: enable_hostname_cmd
-n|--nic-name=string      Required parameter, Interface name, Example: eth1
-c|--ring-count=string    Required parameter, The number of queues for sending and receiving, in JSON format string, example: '{"current": 8}'
```

### Usage Example

```bash
acli network nic queue set --nic-name eth4 --ring-count '{"current": 8}'
```

### Output Example

```bash
task_id: UPID:host-005056b2a30a:00009FD5:3B5A:68F72FB5:Edit Port:20:admin@vtp:
```