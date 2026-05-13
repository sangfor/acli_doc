---
sidebar_position: 1
---

# get

### Overview

View aggregate interface information

### Command Parameters
```bash
-b|--bond-name=string    Required parameter, Aggregate interface name, Example: channel1
```

### Usage Example

```bash
acli network bond get --bond-name channel1
```

### Output Example

```bash
channel1
   addresses:
      ip:
      netmask:
      aliasRole:
   roles:
   enabled: true
   iface_mode: kernel
   link_status: 0
   driver:
   name: channel1
   gateway:
   mac: fe:fb:fe:25:39:b5
   link:
      supportedModes: 9, 2, 0
      autoNegotiation: true
      mode: 0
   members: eth3, eth4
   custom_name:
   mtu: 1500
   type: Bond
   id: channel1
   description:
```