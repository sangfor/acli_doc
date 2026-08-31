---
sidebar_position: 1
---

# list

### Overview

List all NICs and their models of the virtual machine

### Command Parameters

```bash
-v|--vm-id=string    Required parameter, virtual machine ID, example: 614182240912
```

### Usage Example

```bash
acli vm advcfg nictype list -v 614182240912
```

### Output Example

```bash
vmID: 614182240912
nics:
  - nicID: f2d33928-059a-4cd6-9902-ab39cde9189c
    model: e1000
    macAddress: FE:FC:FE:DB:A3:2C
  - nicID: a1b2c3d4-e5f6-7890-1234-567890abcdef
    model: virtio
    macAddress: FE:FC:FE:DB:A3:3D
```
