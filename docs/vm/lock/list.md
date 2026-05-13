---
sidebar_position: 1
---

# list

### 操作概述

获得特定目录下和vm-id有关的锁文件

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机id，示例：1268314679221
```

### 使用示例

```bash
acli vm lock list -v 1268314679221
```

### 结果示例

```bash
[{"lockKey":"vm_1268314679221_host-0050568eefd7:0:1778653821:3060083128703:21001:SAGAFLOW","lockPath":"/cfs/priv/lock/vm_1268314679221/run_host-0050568eefd7:0:1778653821:3060083128703:21001:SAGAFLOW","sagaStatus":"failed","runID":"host-0050568eefd7:0:1778653821:3060083128703:21001:SAGAFLOW","vmid":"1268314679221","filePath":"vm_1268314679221"}]
```
