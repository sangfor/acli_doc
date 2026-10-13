---
sidebar_position: 1
---

# get

### 操作概述

查询虚拟机指定网卡的型号

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机ID，示例：614182240912
-n|--nic-id=string   必要参数，网卡ID，值为 iface_id，示例：f2d33928-059a-4cd6-9902-ab39cde9189c
```

### 使用示例

```bash
acli vm advcfg nictype get -v 614182240912 -n f2d33928-059a-4cd6-9902-ab39cde9189c
```

### 结果示例

```bash
vmID: 614182240912
nicID: f2d33928-059a-4cd6-9902-ab39cde9189c
model: e1000
macAddress: FE:FC:FE:DB:A3:2C
```
