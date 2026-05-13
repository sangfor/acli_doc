---
sidebar_position: 1
---

# list

### Overview

Obtain information about all IB NICs from the specified vendor

### Command Parameters
```bash
-v|--vendor=string    Required parameter, Vendor ID, Example: 0x15ad
```

### Usage Example

```bash
acli network nic rdma list --vendor 0x15ad
```

### Output Example

```bash
Card num:1
Device Information:
     Card         PCIe Function
|----hinic0(CAL_2X25G_LOW)
         |--------0000:41:00.0(NIC:eth4)
         |--------0000:41:00.1(NIC:eth5)
```