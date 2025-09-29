---
sidebar_position: 10
---

# df
操作概述: 调用系统df命令

命令参数:
```bash
无
```

使用示例:
```bash
acli system df
```

结果示例:
```bash
Filesystem  Size  Used Avail Use% Mounted on
overlay      8G  1.8G  5.6G  25% /
/dev/sda3  7.8G  1.8G  5.6G  25% /container-data
/dev/loop2 128K  128K     0 100% /container-data
# ...
```