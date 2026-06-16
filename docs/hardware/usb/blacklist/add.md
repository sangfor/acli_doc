---
sidebar_position: 1
---

# add

### 操作概述

新增USB黑名单

### 命令参数

```bash
-v|--vendor-id=string    必要参数，厂商ID，示例：0409
-p|--product-id=string    必要参数，产品ID，示例：55aa
-n|--name=string          必要参数，设备名称，示例：NEC Corp. Hub SANGFOR USB Hub
```

### 使用示例

```bash
acli hardware usb blacklist add -v 0409 -p 55aa -n "NEC Corp. Hub SANGFOR USB Hub"
```

### 结果示例

```bash
命令执行成功！
```