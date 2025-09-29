---
sidebar_position: 5
---

# session 命名空间
数据面分布式防火墙或虚拟路由器session相关操作

## get命令
操作概述: 查看数据面分布式防火墙或虚拟路由器session

命令参数:  
```bash
-t|--device-type=string 数据面虚拟设备类型: dfw 分布式防火墙, vrouter 虚拟路由器
-n|--device-name=string 数据面分布式防火墙名称或者虚拟路由器id
```

使用示例:
```bash
acli platform service dp session get --device-type vrouter --device-name 2df9fc9e-c067-4d25-b6d6-5c27a10ecff2
```

结果示例:
```bash
host-005056b2ec8d# co t
host-005056b2ec8d(config)#  vrouter 2df9fc9e-c067-4d25-b6d6-5c27a10ecff2
host-005056b2ec8d(config-vrouter)#  show session total
session total number : 0
host-005056b2ec8d(config-vrouter)#
```
