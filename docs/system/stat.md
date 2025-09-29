---
sidebar_position: 10
---

# stat
操作概述: 调用系统stat命令

命令参数:
```bash
无
```

使用示例:
```bash
acli system stat
```

结果示例:
```bash
# acli system stat version
  File: 'version' -> '/boot/firmware/current/package/meta-inf/version'
  Size: 47              Blocks: 1          IO Block: 1024   symbolic link
Device: 8bh/139d        Inode: 810         Links: 1
Access: (0777/lrwxrwxrwx)  Uid: (    0/    root)   Gid: (   50/   staff)
Access: 2025-05-14 04:10:49.000000000
Modify: 2025-05-14 04:10:49.000000000
Change: 2025-05-14 04:10:49.000000000
```