---
sidebar_position: 1
---

# check

### 操作概述

检测磁盘一致性，对比数据库和 CFS 配置的 path 和 size_gib 字段

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机ID，示例：5694620180825
-d|--disk-id=string  可选参数，磁盘ID，不填则检测VM所有磁盘，示例：019e3927-3911-7af1-9768-abb3cd79aa98
```

### 使用示例

```bash
# 检测 VM 所有磁盘
acli vm disk consistency check -v 5694620180825

# 检测指定磁盘
acli vm disk consistency check -v 5694620180825 -d 019e3927-3911-7af1-9768-abb3cd79aa98
```

### 结果示例

```bash
{"code":0,"data":{"checkResult":{"019e3927-3911-7af1-9768-abb3cd79aa98":{"path":{"dbPath":"/disks/ab/b3/019e3927-3911-7af1-9768-abb3cd79aa98/019e3927-3911-7af1-9768-abb3cd79aa98.qcow2","cfsPath":"/disks/ab/b3/019e3927-3911-7af1-9768-abb3cd79aa98/019e3927-3911-7af1-9768-abb3cd79aa98.qcow2","match":true},"size":{"dbSizeGib":10,"cfsSizeGib":10,"match":true}}}}}
```