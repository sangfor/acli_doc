---
sidebar_position: 1
---

# mount

### 操作概述

查看指定存储ID的挂载信息

### 命令参数

```bash
-s|--storage-id=string    必要参数，指定存储id，示例：36000c29a3c9419c600cdb98b5f823744_005056893c9d
```

### 使用示例

```bash
acli storage mount -s 36000c29a3c9419c600cdb98b5f823744_005056893c9d
```

### 结果示例

```bash
/dev/sdb on /sf/data/36000c29a3c9419c600cdb98b5f823744_005056893c9d type sffs (rw,relatime,id=host-005056893c9d,flush=no)
```
