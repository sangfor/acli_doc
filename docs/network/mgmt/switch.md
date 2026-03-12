---
sidebar_position: 1
---

# switch

### 操作概述

切换管理口角色到指定网口

### 命令参数

```bash
-i|--iface=string                   必要参数，新管理口名称，示例：eth2
-c|--carry-ip=integer               是否将现有管理口IP切换到指定网口，默认带IP切换，示例：0(不带IP切换)，1(带IP切换)
```

### 使用示例

```bash
acli network mgmt switch -i eth3

acli network mgmt switch -i eth4 -c 0
```

### 结果示例

```bash
UPID:host-0050568e2936:0000A6D9:655C:69B27910:编辑管理口:3:admin@vtp:
```
