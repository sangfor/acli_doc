---
sidebar_position: 10
---

# list
操作概述: 查看主机网口列表

命令参数:
```bash
无
```

使用示例:
```bash
acli network nic list
```

结果示例:
```bash
eth2.200
   addresses:
      ip:
      netmask:
      aliasRole:
   roles:
   enabled: true
   iface_mode:
   link_status: 0
   driver:
   name: eth2.200
   gateway:
   mac:
   link:
      supportedModes: 9, 2, 0
      autoNegotiation: true
      mode: 0
   members:
   custom_name:
   mtu: 1500
   type: Vlan
   id: eth2.200
   description:

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