---
sidebar_position: 10
---

# get
操作概述: 查看聚合口信息

命令参数:  
```bash
-b|--bond-name=string  必要参数，聚合口名称，例如：channel1
```

使用示例:
```bash
acli network bond get --bond-name channel1
```

结果示例:
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