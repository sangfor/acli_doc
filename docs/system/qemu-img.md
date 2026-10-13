---
sidebar_position: 1
---

# qemu-img

### 操作概述

查询磁盘映像信息与一致性检查（只读，不修复）。

### 命令参数

本命令为部分只读命令，采用封闭式参数白名单（仅列举的参数允许，其余拒绝）。

```bash
info <file>           可选参数，查询磁盘映像信息（只读）
info -f <fmt> <file>  可选参数，指定格式查询磁盘映像信息（只读）
check <file>          可选参数，检查磁盘映像一致性（只读，不修复）
```

写参数禁止清单（命中即拒绝）：

```bash
create                创建磁盘映像（写）
convert               转换磁盘映像格式（写）
resize                调整磁盘映像大小（写）
commit                提交磁盘映像变更（写）
rebase                改变磁盘映像 backing file（写）
snapshot -c/-d/-a/-l  创建/删除/应用/列出快照（写）
```

### 使用示例

```bash
acli system qemu-img info /sf/data/disk.qcow2
```

### 结果示例

```bash
# acli system qemu-img info /sf/data/disk.qcow2
image: /sf/data/disk.qcow2
file format: qcow2
virtual size: 100 GiB (107374182400 bytes)
disk size: 12.5 GiB
cluster_size: 65536
Format specific information:
    compat: 1.1
    lazy refcounts: false
```
