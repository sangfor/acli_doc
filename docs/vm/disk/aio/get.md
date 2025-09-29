---
sidebar_position: 10
---

# get
操作概述: 展示虚拟机磁盘的异步IO模式，当前有native(linux-aio)模式和io_uring模式

命令参数:
```bash
-v|--vm-id=string  虚拟机的ID，例如：2210623695047
-d|--disk=string   虚拟机的磁盘名称，例如：vm-disk-1.qcow2
```

使用示例:
```bash
acli vm disk aio get -v 2749923911666 -d vm-disk-1.qcow2
```

结果示例:
```bash
# 虚拟机使用io_uring模式
io_uring
# 虚拟机使用linux-aio模式
native
# 输入不存在的虚拟机ID或错误的磁盘名称则不会输出内容
```