---
sidebar_position: 2
---

# set

### Overview

Set NIC consistency, modify VN and CFS config based on the specified MAC address (Dangerous operation: will overwrite existing configuration)

### Command Parameters

```bash
-v|--vm-id=string       Required parameter, VM ID. Example: 614182240912
-n|--nic-index=integer  Required parameter, NIC index. Example: 0
-m|--mac=string         Required parameter, force specify MAC address. Example: FE:FC:FE:DB:A3:2C
```

### Usage Example

```bash
acli vm nic consistency set -v 614182240912 -n 0 -m FE:FC:FE:DB:A3:2C
```

### Output Example

```bash
Are you sure you want to execute the operation? (y[es]/n[o]): y
{"VMID":"614182240912","NICIndex":0,"MACBefore":"FE:FC:FE:DB:A3:4C","MACAfter":"FE:FC:FE:DB:A3:2C"}
```