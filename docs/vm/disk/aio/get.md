---
sidebar_position: 1
---

# get

### 操作概述

查看虚拟机指定磁盘的aio信息

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机id，示例：1234567890123
-d|--disk=string     必要参数，虚拟机磁盘名称，示例：vm-disk-1.qcow2
```

### 使用示例

```bash
acli vm disk aio get -v 2749923911666 -d vm-disk-1.qcow2
```

### 结果示例

```bash
# 虚拟机使用io_uring模式
io_uring
# 虚拟机使用linux-aio模式
native
# 输入不存在的虚拟机ID或错误的磁盘名称则不会输出内容
```
