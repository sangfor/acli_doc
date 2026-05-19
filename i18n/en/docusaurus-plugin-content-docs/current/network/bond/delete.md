---
sidebar_position: 1
---

# delete

### Overview

Delete aggregate interface

### Command Parameters
```bash
-h|--hostname=string     Node ID, Example: host-005056b2a30a, Default: enable_hostname_cmd
-n|--bond-name=string    Required parameter, Aggregate interface name, Example: channel1
```

### Usage Example

```bash
acli network bond delete -n channel1
```

### Output Example

```bash
task_id: UPID:host-005056b234ca:0000ACFE:2758:68F8BEAB:Delete aggregation port:1:admin@vtp:
```