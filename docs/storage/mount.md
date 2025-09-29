---
sidebar_position: 10
---

# mount
操作概述: 查看storage-id的本地存储挂载情况

命令参数:
```bash
-s|--storage-id=string    指定存储id，示例：36000c29a3c9419c600cdb98b5f823744_005056893c9d
```

使用示例:
```bash
acli storage mount -s 36000c29a3c9419c600cdb98b5f823744_005056893c9d
```

结果示例:
```bash
/dev/sdb on /sf/data/36000c29a3c9419c600cdb98b5f823744_005056893c9d type sffs (rw,relatime,id=host-005056893c9d,flush=no)
```