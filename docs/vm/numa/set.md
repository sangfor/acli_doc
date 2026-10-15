---
sidebar_position: 2
---

# set

### 操作概述

设置虚拟机指定NUMA绑定位置（配置已写入，需重启生效）

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机id，示例：4872898137715
-n|--nodes=array     必要参数，指定NUMA节点列表，示例：--nodes.1 0 --nodes.2 1
--nodes.N=integer    nodes参数中的每个元素，示例：0
```

### 使用示例

```bash
# 设置虚拟机NUMA绑定到节点0和1
acli vm numa set --vm-id 4872898137715 --nodes.1 0 --nodes.2 1
```

### 结果示例

```bash
code: 0
message: success
```
