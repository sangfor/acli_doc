---
sidebar_position: 10
---

# list
操作概述: 展示虚拟机磁盘镜像是否存在以及状态信息

命令参数:
```bash
-v|--vm-id=string  虚拟机的ID，示例：2210623695047
```

使用示例:
```bash
acli vm disk list -v 2749923911666
```

结果示例:
```bash
total 131076
-rw-r--r-- 1 root root      1241 Aug  5 07:11 4872898137715.conf
-rw------- 1 root root 134217728 Jul 29 17:11 vm-disk-1.qcow2
```