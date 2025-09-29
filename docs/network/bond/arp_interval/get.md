---
sidebar_position: 10
---

# get
操作概述: 获得arp探测的间隔时间

命令参数:
```bash
-b|--bond-name=string  聚合口名称，示例：sf_vs_bond0
```

使用示例:
```bash
acli network bond arp_interval get -b bond0
```

结果示例:
```bash
2000
```