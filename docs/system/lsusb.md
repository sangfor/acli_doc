---
sidebar_position: 1
---

# lsusb

### 操作概述

查询 USB 设备信息

### 命令参数

```bash
-v|--verbose=flag   显示设备详细信息
-s=string          按总线/设备号过滤（格式：[[bus]:][devnum]）
-d=string          按厂商/产品 ID 过滤（格式：vendor:[product]）
-t|--tree=flag      以树形结构显示设备
-V|--version=flag   显示版本信息
-h|--help=flag      显示帮助信息
```

### 使用示例

```bash
acli system lsusb -v
```

### 结果示例

```bash
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
```
