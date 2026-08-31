---
sidebar_position: 1
---

# list

### 操作概述

列出虚拟机全部网卡及型号

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机ID，示例：614182240912
```

### 使用示例

```bash
acli vm advcfg nictype list -v 614182240912
```

### 结果示例

```bash
vmID: 614182240912
nics:
  - nicID: f2d33928-059a-4cd6-9902-ab39cde9189c
    model: e1000
    macAddress: FE:FC:FE:DB:A3:2C
  - nicID: a1b2c3d4-e5f6-7890-1234-567890abcdef
    model: virtio
    macAddress: FE:FC:FE:DB:A3:3D
```
