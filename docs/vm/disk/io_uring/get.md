---
sidebar_position: 1
---

# get

### 操作概述

CPU使用情况(%表示,如输出100即为占用100%CPU资源,即一个逻辑核)

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机id，示例：1234567890123
```

### 使用示例

```bash
acli vm disk io_uring get -v 2749923911666
```

### 结果示例

```bash
# %表示,如输出100%即为占用一个逻辑核
CPU Usage: 20.8%
# 输入不存在的虚拟机ID则不会输出内容
```
