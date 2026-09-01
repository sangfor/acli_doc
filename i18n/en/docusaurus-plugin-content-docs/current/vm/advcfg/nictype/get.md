---
sidebar_position: 1
---

# get

### Overview

Query the model of the specified NIC on the virtual machine

### Command Parameters

```bash
-v|--vm-id=string    Required parameter, virtual machine ID, example: 614182240912
-n|--nic-id=string   Required parameter, NIC ID, value is iface_id, example: f2d33928-059a-4cd6-9902-ab39cde9189c
```

### Usage Example

```bash
acli vm advcfg nictype get -v 614182240912 -n f2d33928-059a-4cd6-9902-ab39cde9189c
```

### Output Example

```bash
vmID: 614182240912
nicID: f2d33928-059a-4cd6-9902-ab39cde9189c
model: e1000
macAddress: FE:FC:FE:DB:A3:2C
```
