---
sidebar_position: 1
---

# get

### Overview

Query the WWN (World Wide Name, a unique disk identifier) of the specified virtual machine disk

### Command Parameters

```bash
-v|--vm-id=string      Required parameter, virtual machine ID, example: 614182240912
-d|--disk-id=string    Required parameter, disk ID (UUID), example: 01a03ddf-5148-727d-9e9c-e8e581df7088 (obtainable via vm advcfg wwn list)
```

### Usage Example

```bash
acli vm advcfg wwn get -v 614182240912 -d 01a03ddf-5148-727d-9e9c-e8e581df7088
```

### Output Example

```bash
vmID: 614182240912
disk:
  diskID: 01a03ddf-5148-727d-9e9c-e8e581df7088
  diskName: VirtioScsi0
  busName: virtio-scsi
  bootdisk: true
  wwn: 6000c29a3b7e4f18a1b2c3d4e5f60718
```