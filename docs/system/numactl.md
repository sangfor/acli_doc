---
sidebar_position: 1
---

# numactl

### 操作概述

查询 NUMA 拓扑和策略

### 命令参数

```bash
-H|--hardware=flag  显示 NUMA 硬件拓扑（无参数时默认）
-s|--show=flag      显示当前 NUMA 策略
```

### 使用示例

```bash
acli system numactl --hardware
acli system numactl --show
```

### 结果示例

```bash
available: 1 nodes (0)
node 0 cpus: 0 1 2 3 4 5 6 7
node 0 size: 39617 MB
node 0 free: 18712 MB
node distances:
node   0 
  0:  10 
```
