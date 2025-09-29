---
sidebar_position: 10
---

# get
操作概述: 根据虚拟机id获得虚拟机路径

命令参数:
```bash
-v|--vm-id=string  虚拟机的ID，例如：1072335336316
```

使用示例:
```bash
acli vm disk path get -v 1072335336316
```

结果示例:
```bash
/sf/data/a4ef106e_vs_vol_rep2/images/cluster/1072335336316.vm
```