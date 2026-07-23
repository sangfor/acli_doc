---
sidebar_position: 1
---

# list

### 操作概述

列出指定节点上所有已设置 device 级 multipath 自定义配置的厂商型号、自定义参数及同型号存储列表。

### 命令参数

```bash
-n|--hostname=string    可选参数，目标主机名，缺省为当前节点，示例：host-xxxx
```

### 使用示例

```bash
acli system multipathconfig devicepolicy list -n host-xxxx
```

### 结果示例

```bash
    custom_params                |product        |storages                                             |vendor 
    -----------------------------|---------------|-----------------------------------------------------|-------
1   path_checker readsector0     |PowerStore|368ccf09800fec26a86bd45b6b76bc498 (PowerStore-01)    |DellEMC
    path_grouping_policy failover|               |                                                     |
```
