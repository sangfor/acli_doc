---
sidebar_position: 1
---

# down

### Overview

Disable physical interface

### Command Parameters
```bash
-n|--nic-name=string    Required parameter, Interface name, Example: eth1
-h|--hostname=string    Node ID, default value, and current node ID, Example: host-005056893c9d, Default: enable_hostname_cmd
```

### Usage Example

```bash
acli network nic down --hostname host-005056b2ec8d --nic-name eth2
```

### Output Example

```bash
task_id: UPID:host-005056b2ec8d:00009AFB:1ADD4A0:6874A955:Edit Port:10:admin@vtp:
```