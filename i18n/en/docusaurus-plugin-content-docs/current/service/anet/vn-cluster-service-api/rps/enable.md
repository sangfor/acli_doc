---
sidebar_position: 1
---

# enable

### Overview

Enable RPS on the node

### Command Parameters
```bash
-h|--hosts=array    Required parameter, Node ID list, Example: -h.1 host-005056894c2e -h.2 host-00505689413s
--hosts.N=string    Each element in the hosts parameter, Example: host-005056894c2e
```

### Usage Example

```bash
acli service anet vn-cluster-service-api rps enable -h.1 host-002987263c8g -h.2 host-761846915f3m
```

### Output Example

```bash
taskId: host-005056b2ec8d:00009AFB:1ADD4A0:6874A955
```