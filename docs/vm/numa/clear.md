---
sidebar_position: 3
---

# clear

### 操作概述

清除虚拟机自定义NUMA绑定，回退智能NUMA调度（重启生效）

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机id，示例：4872898137715
```

### 使用示例

```bash
# 清除虚拟机的自定义NUMA绑定
acli vm numa clear -v 4872898137715
```

### 结果示例

```bash
code: 0
message: success
```
