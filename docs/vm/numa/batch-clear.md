---
sidebar_position: 5
---

# batch-clear

### 操作概述

批量清除虚拟机自定义NUMA绑定，回退智能NUMA调度（逐台处理，部分成功部分失败并列出失败原因，重启生效）

### 命令参数

```bash
-v|--vm-ids=array    必要参数，虚拟机id列表，示例：--vm-ids.1 7369491980128 --vm-ids.2 7291549938786
--vm-ids.N=string    vm-ids参数中的每个元素，示例：7291549938786
```

### 使用示例

```bash
# 批量清除两台虚拟机的自定义NUMA绑定
acli vm numa batch-clear --vm-ids.1 7369491980128 --vm-ids.2 7291549938786
```

### 结果示例

```bash
code: 0
message: success
```
