---
sidebar_position: 1
---

# get

### 操作概述

查询指定节点上指定存储实际生效的多路径策略。

### 命令参数

```bash
-n|--hostname=string    可选参数，目标主机名，缺省为当前节点，示例：host-xxxx
-w|--wwid=string         必要参数，逻辑存储 WWID，示例：3648bd4a100fa95b6550a2d9c000002ac
```

### 使用示例

```bash
acli system multipathconfig get -n host-xxxx -w 3648bd4a100fa95b6550a2d9c000002ac
```

### 结果示例

```bash
    device                       |multipath
    -----------------------------|---------
1   path_checker readsector0     |         
    path_grouping_policy failover|         
    product PowerStore      |         
    vendor DellEMC               |
```
