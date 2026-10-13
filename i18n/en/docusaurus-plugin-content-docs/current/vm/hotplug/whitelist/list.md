---
sidebar_position: 5
---

# list

### Overview

Query the OS whitelist for CPU/memory hot-add and global default policy status

### Command Parameters

None

### Usage Example

```bash
acli vm hotplug whitelist list
```

### Output Example

```bash
    Distribution  |Hot-add CPU|Hot-add Memory
    --------------|-----------|--------------
1   Ubuntu 14,64  |true       |true         
2   All unknown   |false      |false      
```
