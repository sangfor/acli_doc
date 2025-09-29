---
sidebar_position: 10
---

# list
操作概述: 查看cpu中断核相关信息

命令参数:
```bash
无
```

使用示例:
```bash
acli network nic irqcpu list
```

结果示例:
```bash
eth0
   irqs: 59, 60, 61, 62, 63, 64, 65, 66, 67
   cpus: 3
   iface_name: eth0

eth2
   irqs: 77, 78, 79, 80, 81, 82, 83, 84, 85
   cpus: 2
   iface_name: eth2

eth3
   irqs: 86, 87, 88, 89, 90, 91, 92, 93, 94
   cpus: 4
   iface_name: eth3

eth4
   irqs: 95, 96, 97, 98, 99, 100, 101, 102, 103
   cpus: 1
   iface_name: eth4

eth5
   irqs: 104, 105, 106, 107, 108, 109, 110, 111, 112
   cpus: 6
   iface_name: eth5

p_eth1
   irqs: 68, 69, 70, 71, 72, 73, 74, 75, 76
   cpus: 7
   iface_name: p_eth1
```