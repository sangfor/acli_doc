---
sidebar_position: 2
---

# sync

### 操作概述

同步磁盘配置，根据传入的路径和大小同时修改 CFS 和 DB（危险操作：会覆盖现有配置）

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机ID，示例：5694620180825
-d|--disk-id=string  必要参数，磁盘ID，示例：019e3927-3911-7af1-9768-abb3cd79aa98
-p|--path=string     可选参数，强制指定路径，示例：/cfs/nodes/5694620180825/test.qcow2
-s|--size=integer    可选参数，强制指定大小GiB，示例：100
```

### 使用示例

```bash
# 只同步路径（CFS 和 DB）
acli vm disk consistency sync -v 5694620180825 -d 019e3927-3911-7af1-9768-abb3cd79aa98 -p /cfs/nodes/5694620180825/test.qcow2

# 只同步大小（CFS 和 DB）
acli vm disk consistency sync -v 5694620180825 -d 019e3927-3911-7af1-9768-abb3cd79aa98 -s 100

# 同时同步路径和大小
acli vm disk consistency sync -v 5694620180825 -d 019e3927-3911-7af1-9768-abb3cd79aa98 -p /disks/ab/b3/019e3927-3911-7af1-9768-abb3cd79aa98/019e3927-3911-7af1-9768-abb3cd79aa98.qcow2 -s 10
```

### 结果示例

```bash
Are you sure you want to execute the operation? (y[es]/n[o]): y
{"diskID":"019e3927-3911-7af1-9768-abb3cd79aa98","pathBefore":"/disks/ab/b3/019e3927-3911-7af1-9768-abb3cd79aa98/019e3927-3911-7af1-9768-abb3cd79aa98.qcow2","pathAfter":"/disks/ab/b3/019e3927-3911-7af1-9768-abb3cd79aa98/019e3927-3911-7af1-9768-abb3cd79aa98.qcow2","sizeGibBefore":10,"sizeGibAfter":10}
```