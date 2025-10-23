---
sidebar_position: 10
---

# set
操作概述: 设置主机网口

命令参数:
```bash
-h|--hostname=string 主机id，示例：host-005056893c9d
-n|--nic-name=string 网口名字，示例：eth1
-i|--ip=string 网口ip，示例：192.168.0.5
-m|--netmask=string 网口ip掩码，示例：255.255.255.0
-g|--gateway=string 网关，示例：192.168.0.1
-l|--link-mode=integer 网口速率，枚举值： 0（10baseT-HD）, 1（10baseT-FD）, 2（100baseT-HD）, 3（100baseT-FD）, 4（1000baseT-HD）, 5（1000baseT-FD）, 15（2500baseT-FD）, 17（5000baseT-FD）, 6（autonegotiation）, 12（10000baseT-FD）, 21（20000baseMLD2-FD）, 22（20000baseKR2-FD）, 23（40000baseKR4-FD）, 24（40000baseCR4-FD）, 25（40000baseSR4-FD）, 26（40000baseLR4-FD）, 31（25000baseCR-FD）, 32（25000baseKR-FD）, 33（25000baseSR-FD）, 34（50000baseCR2-FD）, 35（50000baseKR2-FD）, 36（100000baseKR4-FD）, 37（100000baseCR4-FD）, 38（100000baseSR4-FD）, 39（100000baseLR4ER4-FD）, 40（50000baseSR4-FD）
```

使用示例:
```bash
acli network nic set --nic-name eth4 --link-mode 12
```

结果示例:
```bash
task_id: UPID:host-005056b2a30a:00009FD5:3B5A:68F9E5AD:编辑网口:64:admin@vtp:
```
