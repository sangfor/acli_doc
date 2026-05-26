---
sidebar_position: 2
---

# set

### 操作概述

设置网卡一致性，根据指定的 MAC 地址修改 VN 和 CFS 配置（危险操作：会覆盖现有配置）

### 命令参数

```bash
-v|--vm-id=string       必要参数，虚拟机ID，示例：614182240912
-n|--nic-index=integer  必要参数，网卡索引，示例：0
-m|--mac=string         必要参数，强制指定MAC地址，示例：FE:FC:FE:DB:A3:2C
```

### 使用示例

```bash
acli vm nic consistency set -v 614182240912 -n 0 -m FE:FC:FE:DB:A3:2C
```

### 结果示例

```bash
您确定要执行这个操作? (y[es]/n[o]): y
{"VMID":"614182240912","NICIndex":0,"MACBefore":"FE:FC:FE:DB:A3:4C","MACAfter":"FE:FC:FE:DB:A3:2C"}
```
