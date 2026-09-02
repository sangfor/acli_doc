---
sidebar_position: 1
---

# lspci

### 操作概述

查看主机 PCI 设备信息

### 命令参数

```bash
-n  以数字形式显示厂商和设备 ID
-v  显示设备的详细信息
-k  显示设备对应的内核驱动
-d  按厂商/设备 ID 过滤设备
```

### 使用示例

```bash
acli system lspci -v
```

### 结果示例

```bash
00:00.0 Host bridge: Intel Corporation Device 2020 (rev 06)
        Subsystem: Intel Corporation Device 2020
        Flags: bus master, fast devsel, latency 0
        Capabilities: [e0] Vendor Specific Information: Len=14 <?>

00:01.0 PCI bridge: Intel Corporation Device 2030 (rev 06)
        Flags: bus master, fast devsel, latency 0
        Bus: primary=00, secondary=01, subordinate=01, sec-latency=0
        ...
```
