---
sidebar_position: 1
---

# lsusb

### 操作概述

查询 USB 设备信息

### 命令参数

命令格式：

```bash
acli system lsusb [options]...
```

```bash
-v|--verbose=flag  显示设备详细信息
-s=string          按总线/设备号过滤（十进制，格式：[[bus]:][devnum]）
-d=string          按厂商/产品 ID 过滤（十六进制，格式：vendor:[product]）
-D=string          指定要检查的 USB 设备文件
-t|--tree=flag     以树形结构显示设备
-V|--version=flag  显示版本信息
-h|--help=flag     显示帮助信息
```

### 使用示例

```bash
acli system lsusb -h
```

### 结果示例

```bash
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
```

执行 `acli system lsusb -h` 返回以下帮助信息：

```text
Usage: lsusb [options]...
List USB devices
  -v, --verbose
      Increase verbosity (show descriptors)
  -s [[bus]:][devnum]
      Show only devices with specified device and/or
      bus numbers (in decimal)
  -d vendor:[product]
      Show only devices with the specified vendor and
      product ID numbers (in hexadecimal)
  -D device
      Selects which device lsusb will examine
  -t, --tree
      Dump the physical USB device hierarchy as a tree
  -V, --version
      Show version of program
  -h, --help
      Show usage and help
```
