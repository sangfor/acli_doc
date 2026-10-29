---
sidebar_position: 1
---

# clview

### 操作概述

查看设备的心跳头、心跳块和锁块数据，以及文件的锁持有者信息。

### 命令参数

命令格式：

```bash
acli system clview [OPTION]* DEVICE
```

`DEVICE` 为必要参数，指定要查询的设备，例如 `/dev/sdc`。选项含义可参考工具返回的帮助信息（见结果示例）。

数据以十六进制和十进制两种格式展示。查看结果时需留意括号内的状态信息，例如 `right`、`wrong`、`free`、`sh`、`ex`。

### 使用示例

```bash
acli system clview
```

### 结果示例

未指定设备时返回以下提示和帮助信息，其中 `cl_tool_view` 为底层工具名称：

```text
No device specified
Usage: cl_tool_view [OPTION]* DEVICE

Options:
  -p, --pno=N                The address of disk, it's unit is m.
  -s, --sector=N             Read N-th sector (default: 4096)
  -n, --count=N             how many sectors to show(default: 1)
  -t, --type=TYPE           The type of the block data. There are three values, h(heartbeat header), b(heartbeat block), l(lock block). If it is not specified, the application will judge it based on sector block data by self
  -q, --query-lock-holders    Query the lock-holders of the given file
  -h, --help                 Show this message and exit

It uses two types of formats to display data, hexadecimal and decimal. And you need to note the parentheses prompted state information, such as "right" or "wrong", "free", "sh", "ex" and so on.

Simple example: Read the third sector block data on /dev/sdc
  cl_tool_view -s 3 /dev/sdc
```
