---
sidebar_position: 1
---

# get

### Overview

Query the custom SMBIOS manufacturer information (manufacturer) of the virtual machine and its enable switch status

### Command Parameters

```bash
-v|--vm-id=string  Required parameter, virtual machine ID, example: 614182240912
```

### Usage Example

```bash
acli vm advcfg smbios get -v 614182240912
```

### Output Example

```bash
enabled: true
manufacturer: HPE
vmID: 614182240912
```