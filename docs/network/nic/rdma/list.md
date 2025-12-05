---
sidebar_position: 10
---

# list
操作概述: 获取指定厂商的所有ib网卡设备

命令参数:
```bash
-v|--vendor=string        必要参数，厂商id，示例：0x15ad
```

使用示例:
```bash
acli network nic rdma list --vendor 0x15ad
```

结果示例:
```bash
Card num:1
Device Information:
     Card         PCIe Function
|----hinic0(CAL_2X25G_LOW)
         |--------0000:41:00.0(NIC:eth4)
         |--------0000:41:00.1(NIC:eth5)
```