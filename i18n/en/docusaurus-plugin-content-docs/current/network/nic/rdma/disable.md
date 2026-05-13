---
sidebar_position: 1
---

# disable

### Overview

Disable RDMA for the specified IB NIC from the specified vendor

### Command Parameters
```bash
-v|--vendor=string    Required parameter, Vendor ID, Example: 0x15ad
-i|--ib-dev=string    Required parameter, IB NIC name, Example: hinic0
```

### Usage Example

```bash
acli network nic rdma disable --vendor 0x15ad --ib-dev hinic0
```

### Output Example

```bash
***************** Current Info *******************
[Current   ] Cfg template index :  0
***************** Next Reset Cfg *****************
[Next Reset] Max support index  :  3
[Next Reset] Cfg template index :  2
[Next Reset] Firmware support cfg template name:
             Template[ 0]: NIC_2X25G
             Template[ 1]: NIC_2X25G_3PF_120VF
             Template[ 2]: ROCE_2X25G
             Template[ 3]: NIC_2X25G_4PF
```