---
sidebar_position: 1
---

# check

### Overview

Check RDMA whitelist configuration

### Command Parameters

```bash
-t|--type=string                    Required parameter,Configuration type. Enumeration values: vs (storage private network), external_storage (external storage)
-m|--multi-node=boolean             Collect information from all nodes. Enumeration values: true/false. Default value: true
-T|--table=boolean                  Display results in table format. Enumeration values: true/false. Default value: true
```

### Usage Example

```bash
acli network nic rdma whitelist check -t vs
```

### Output Example

```bash
desc                                                    | vendor_id | device_id | ip_list                   | compatible
--------------------------------------------------------+-----------+-----------+---------------------------+-----------
VMware VMXNET3 Ethernet Controller [15ad:07b0] (rev 01) | 0x15ad    | 0x07b0    | 10.131.136.7,10.131.136.8 | false
```
