---
sidebar_position: 1
---

# set

### Overview

Update RDMA whitelist configuration

### Command Parameters

```bash
-d|--device-id=string               Required parameter,Device ID, used to identify the NIC model. Example: 0x1017
-v|--vendor-id=string               Required parameter,Vendor ID, used to identify the NIC manufacturer. Example: 0x15b3
-i|--ip-list=string                 List of node IPs to be updated. Example: 10.103.17.10,10.113.18.11
-t|--type=string                    Required parameter,Configuration type. Enumeration values: vs (storage private network), external_storage (external storage)
-T|--table=boolean                  Display results in table format. Enumeration values: true/false. Default value: true

```

### Usage Example

```bash
acli network nic rdma whitelist set -d 0x07b0 -v 0x15ad -i 10.131.136.7,10.131.136.8 -t vs
```

### Output Example

```bash
IP           | CPU Arch | Associated Interfaces         | Success
-------------+----------+-------------------------------+--------
10.131.136.7 | x86_64   | eth0,eth1,eth2,eth3,eth4,eth5 | true
10.131.136.8 | x86_64   | eth0,eth1,eth2,eth3,eth4,eth5 | true
```
