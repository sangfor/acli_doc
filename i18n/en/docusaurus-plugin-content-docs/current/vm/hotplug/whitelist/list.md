---
sidebar_position: 5
---

# list

### Overview

Query the OS whitelist allowing CPU/memory hot-add and the global fallback status

### Command Parameters

None

### Usage Example

```bash
acli vm hotplug whitelist list
```

### Output Example

```bash
    OS Distribution | Hot-add CPU | Hot-add Memory
    ------------|---------|----------
1   Ubuntu 14,64|√        |√         
2   All unknown |×        |×         
```
