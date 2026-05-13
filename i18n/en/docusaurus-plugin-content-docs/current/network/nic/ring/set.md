---
sidebar_position: 1
---

# set

### Overview

Configure ring buffer parameters for the current interface

### Command Parameters
```bash
-h|--hostname=string       Node ID, default value, and current node ID, Example: host-005056893c9d, Default: enable_hostname_cmd
-n|--nic-name=string       Required parameter, Interface name, Example: eth1
-b|--ring-buffer=string    Required parameter, Set the current ring buffer parameters for the network port, in JSON format string, example: '{"current": {"rx": 4096, "tx": 4096}}'
```

### Usage Example

```bash
acli network nic ring set --nic-name eth4 --ring-buffer '{"current": {"rx": 4096, "tx": 4096}}'
```

### Output Example

```bash
task_id: UPID:host-005056b2a30a:00009FD5:3B5A:68F732C6:Edit Port:28:admin@vtp:
```