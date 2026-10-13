---
sidebar_position: 1
---

# realethtool

### 操作概述

realethtool命令

### 命令参数

```bash
-S|--statistics=flag  查看网卡的统计信息
-i|--driver=flag      查看网卡对应的驱动信息
-a|--all=flag         查看网卡的所有信息
<iface>               必要参数，指定要查看的网卡名（需在白名单接口内），示例：eth0
```

### 使用示例

```bash
acli system realethtool eth0
```

```bash
acli system realethtool -i eth0
```

### 结果示例

```bash
# acli system realethtool eth0
Settings for eth0:
        Supported ports: [ TP ]
        Supported link modes:   1000baseT/Full
                                10000baseT/Full
        Supported pause frame use: No
        Supports auto-negotiation: No
        Supported FEC modes: Not reported
        Advertised link modes:  Not reported
        Advertised pause frame use: No
        Advertised auto-negotiation: No
        Advertised FEC modes: Not reported
        Speed: 10000Mb/s
        Duplex: Full
        Port: Twisted Pair
        PHYAD: 0
        Transceiver: internal
        Auto-negotiation: off
        MDI-X: Unknown
        Supports Wake-on: uag
        Wake-on: d
        Link detected: yes
```
