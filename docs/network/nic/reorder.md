---
sidebar_position: 10
---

# reorder
操作概述: 调整网口顺序

命令参数:
```bash
-b|--before=string 调整前网口列表，示例：eth0 eth1 eth2
-a|--after=string 调整后网口列表，示例：eth2 eth1 eth0
```

使用示例:
```bash
acli network nic reorder --before "eth0 eth1 eth2 eth3 eth4 eth5" --after "eth0 eth1 eth2 eth3 eth4 eth5"
```

结果示例:
```bash

```
