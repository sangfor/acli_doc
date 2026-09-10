---
sidebar_position: 1
---

# list

### Overview

List fault domains of the specified volume

### Command Parameters

```bash
-v|--volume-id=string   Required parameter, VS volume ID, example: 8a83211f_vs_vol_rep3
-i|--id=string          Fault domain ID (optional). When provided, only the fault domain with this ID is returned; "can not find id <id>" is output if not found. When omitted, returns a JSON array of all fault domains, example: 1
```

### Usage Example

```bash
acli storage vsmgr fault-domains list --volume-id 8a83211f_vs_vol_rep3
```

### Output Example

```bash
[
    {
        "name": "domain1",
        "id": 0,
        "hosts": [
            "host-105056913a04",
            "host-105056913a05"
        ]
    },
    {
        "name": "domain2",
        "id": 1,
        "hosts": [
            "host-105056913a06",
            "host-105056913a07"
        ]
    }
]
```

With `--id` filter, returns a single object (without the outer array).
