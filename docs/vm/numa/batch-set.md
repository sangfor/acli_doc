---
sidebar_position: 4
---

# batch-set

### 操作概述

批量设置虚拟机指定NUMA绑定位置（逐台校验，部分成功部分失败并列出失败原因，重启生效）

### 命令参数

```bash
-v|--vm-ids=array    必要参数，虚拟机id列表，示例：--vm-ids.1 7369491980128 --vm-ids.2 7291549938786
--vm-ids.N=string    vm-ids参数中的每个元素，示例：7291549938786
-n|--nodes=array     必要参数，统一指定NUMA节点列表，示例：--nodes.1 0 --nodes.2 1
--nodes.N=integer    nodes参数中的每个元素，示例：0
```

### 使用示例

```bash
# 批量设置两台虚拟机的NUMA绑定到节点0和1
acli vm numa batch-set --vm-ids.1 7369491980128 --vm-ids.2 7291549938786 --nodes.1 0 --nodes.2 1
```

### 结果示例

```bash
code: 0
message: success
```
