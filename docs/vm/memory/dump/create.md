---
sidebar_position: 10
---

# create
操作概述: 创建dump虚拟机内存任务

命令参数:
```bash
-v|--vm-id=string  虚拟机id，示例：4872898137715
-p|--path=string   虚拟机内存dump存储目录，注意：剩余存储空间必须是虚拟机内存的两倍以上。一般建议虚拟存储路径，比如：/sf/data/e8b0e860_vs_vol_rep2，20GB的虚拟机dump之后大约花费15分钟
```

使用示例:
```bash
acli vm memory dump create -v 4872898137715 -p /sf/data/e8b0e860_vs_vol_rep2
```

结果示例:
```bash
dump虚拟机内存成功!
```
