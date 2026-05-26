---
sidebar_position: 2
---

# set

### 操作概述

设置CPU一致性，根据指定的插槽数和每插槽核心数修改 DB 和 CFS 配置（危险操作：会覆盖现有配置）

### 命令参数

```bash
-v|--vm-id=string                 必要参数，虚拟机ID，示例：614182240912
-s|--sockets=integer              可选参数，强制指定CPU插槽数，示例：2
-c|--cores-per-socket=integer     可选参数，强制指定每插槽核心数，示例：1
```

### 使用示例

```bash
# 同时设置插槽数和每插槽核心数
acli vm cpu consistency set -v 614182240912 -s 2 -c 1

# 只设置插槽数
acli vm cpu consistency set -v 614182240912 -s 1
```

### 结果示例

```bash
您确定要执行这个操作? (y[es]/n[o]): y
{"VMID":"614182240912","SocketsBefore":1,"SocketsAfter":2,"CoresPerSocketBefore":1,"CoresPerSocketAfter":1}
```