---
sidebar_position: 10
---

# get
操作概述: 展示虚拟机io_uring当前状态，目前只支持显示虚拟机io_uring的CPU使用率

命令参数:
```bash
-v|--vm-id=string  虚拟机的ID，例如：2210623695047
```

使用示例:
```bash
acli vm disk io_uring get -v 2749923911666
```

结果示例:
```bash
# %表示,如输出100%即为占用一个逻辑核
CPU Usage: 20.8%
# 输入不存在的虚拟机ID则不会输出内容
```