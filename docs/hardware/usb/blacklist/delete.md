---
sidebar_position: 1
---

# delete

### 操作概述

删除USB黑名单

### 命令参数

```bash
-v|--vendor-id=string    必要参数，厂商ID，示例：0409
-p|--product-id=string    必要参数，产品ID，示例：55aa
```

### 使用示例

```bash
acli hardware usb blacklist delete -v 0409 -p 55aa
```

### 结果示例

```bash
命令执行成功！
```