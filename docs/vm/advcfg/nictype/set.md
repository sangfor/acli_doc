---
sidebar_position: 1
---

# set

### 操作概述

修改虚拟机指定网卡的型号（仅支持关机状态下修改）

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机ID，示例：614182240912
-n|--nic-id=string   必要参数，网卡ID，值为 iface_id，示例：f2d33928-059a-4cd6-9902-ab39cde9189c
-t|--type=string     必要参数，目标网卡型号，枚举值：virtio（virtio 半虚拟化网卡，性能更优，需 Guest OS 安装 virtio 驱动）或 e1000（Intel 82540EM 模拟千兆网卡，兼容性更好），大小写不敏感，示例：virtio
```

### 使用示例

```bash
acli vm advcfg nictype set -v 614182240912 -n f2d33928-059a-4cd6-9902-ab39cde9189c -t virtio
```

### 结果示例

```bash
您确定要执行这个操作? (y[es]/n[o]): y
vmID: 614182240912
nicID: f2d33928-059a-4cd6-9902-ab39cde9189c
modelBefore: e1000
modelAfter: virtio
taskID: host-005056b2894b:280998:1760441353:6913569233831
warning: null
```
