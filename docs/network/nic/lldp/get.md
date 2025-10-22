---
sidebar_position: 10
---

# get
操作概述: 展示网口lldp

命令参数:  
```bash
-n|--nic-name 网口名称，示例：eth1
```

使用示例:
```bash
acli network nic lldp get --nic-name eth2
```

结果示例:
```bash
hasMultiNeighbors: 0
ifaceName: eth2
local:
    aggregationNum: 0
    maxFrameSize: 1518
    vlanId: 0
mode: RXTX
enabled: 1
```
