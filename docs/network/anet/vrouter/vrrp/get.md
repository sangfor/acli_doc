---
sidebar_position: 10
---

# get
操作概述: 查看路由器vrrp配置

命令参数:  
```bash
-r|--router-id=string               必要参数，路由器id，例如：3e1be084-e194-417e-a30d-652c3b415143
```

使用示例:
```bash
acli network anet vrouter vrrp get --router-id 2df9fc9e-c067-4d25-b6d6-5c27a10ecff2
```

结果示例:
```bash
host-005056b2ec8d# co t
host-005056b2ec8d(config)#  vrouter 2df9fc9e-c067-4d25-b6d6-5c27a10ecff2
host-005056b2ec8d(config-vrouter)#  show vrrp
========================================================================================================================
vrouter_name                             vrrpid     enable     status     ha-link
------------------------------------------------------------------------------------------------------------------------
2df9fc9e-c067-4d25-b6d6-5c27a10ecff2     1          yes        backup     7e7f9c7c-8b56-4327-b61e-53e45f0b1137
========================================================================================================================
host-005056b2ec8d(config-vrouter)#
```