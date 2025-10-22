---
sidebar_position: 10
---

# get
操作概述: 查看数据面分布式防火墙或虚拟路由器session

命令参数:  
```bash
-t|--device-type=string             必要参数，数据面虚拟设备类型：dfw(分布式防火墙), vrouter(虚拟路由器)
-n|--device-name=string             必要参数，数据面分布式防火墙名称（例如：dfw_dcc6c377-24ff-4389-8762-13132c29dbe9）或者虚拟路由器id（例如：3e1be084-e194-417e-a30d-652c3b415143）

```

使用示例:
```bash
acli network anet session get --device-type vrouter --device-name 2df9fc9e-c067-4d25-b6d6-5c27a10ecff2
```

结果示例:
```bash
host-005056b2ec8d# co t
host-005056b2ec8d(config)#  vrouter 2df9fc9e-c067-4d25-b6d6-5c27a10ecff2
host-005056b2ec8d(config-vrouter)#  show session total
session total number : 0
host-005056b2ec8d(config-vrouter)#
```