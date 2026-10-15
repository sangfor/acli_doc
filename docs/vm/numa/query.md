---
sidebar_position: 1
---

# query

### 操作概述

查询虚拟机NUMA绑定位置（支持单台与主机运行中查询）

### 命令参数

```bash
-v|--vm-id=string    可选参数，虚拟机id（与--host二选一），示例：4872898137715
-H|--host-id=string  可选参数，主机id（与--vm二选一），仅返回运行中虚拟机，示例：host-0050568eecc7
```

### 使用示例

```bash
# 查询单台虚拟机的NUMA绑定位置
acli vm numa query -v 4872898137715

# 查询主机上所有运行中虚拟机的NUMA绑定位置
acli vm numa query -H host-0050568eecc7
```

### 结果示例

```bash
vmID: 4872898137715
name: test-vm
vcpuCount: 8
numaEnabled: true
numaNodes:
  0
  1
runningNumaNodes:
  0
bindStatus: user
```
