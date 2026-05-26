---
sidebar_position: 2
---

# set

### 操作概述

设置内存一致性，根据指定的内存大小修改 DB 和 CFS 配置（危险操作：会覆盖现有配置）

### 命令参数

```bash
-v|--vm-id=string         必要参数，虚拟机ID，示例：614182240912
-m|--memory-mb=integer   必要参数，强制指定内存大小MB，示例：2048
```

### 使用示例

```bash
acli vm memory consistency set -v 614182240912 -m 2048
```

### 结果示例

```bash
您确定要执行这个操作? (y[es]/n[o]): y
{"VMID":"614182240912","MemoryMBBefore":4096,"MemoryMBAfter":2048}
```