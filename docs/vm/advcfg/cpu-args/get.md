---
sidebar_position: 1
---

# get

### 操作概述

查询虚拟机CPU的自定义 qemu 开机参数

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机ID，示例：6520699837375
```

### 使用示例

```bash
acli vm advcfg cpu-args get -v 6520699837375
```

### 结果示例

未设置时：

```bash
customArgs:
vmID: 6520699837375
```

已设置时：

```bash
customArgs: hv_vendor_id=CustomOEM
vmID: 6520699837375
```