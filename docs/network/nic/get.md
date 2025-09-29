---
sidebar_position: 10
---

# get
操作概述: 查看主机网口信息

命令参数:
```bash
-n|--nic-name 网口名字
```

使用示例:
```bash
acli network nic get --nic-name eth0
```

结果示例:
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