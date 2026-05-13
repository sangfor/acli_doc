---
sidebar_position: 1
---

# get

### Overview

View node interface information

### Command Parameters
```bash
-n|--nic-name=string    Required parameter, Port name, example: eth1
```

### Usage Example

```bash
acli network nic get --nic-name eth0
```

### Output Example

```bash
eth0
   addresses:
      ip: 10.131.201.210
      netmask: 255.255.240.0
      aliasRole:
   roles: Tercom, Mgmt
   enabled: true
   iface_mode: kernel
   link_status: 0
   driver: vmxnet3
   name: eth0
   gateway: 10.131.192.1
   mac: 00:50:56:b2:ec:8d
   link:
      supportedModes: 9, 2, 0
      autoNegotiation: true
      mode: 0
   members:
   custom_name:
   mtu: 1500
   type: Physical
   id: eth0
   description:
```