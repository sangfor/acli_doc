---
sidebar_position: 1
---

# get

### 操作概述

查询虚拟机整机的自定义 qemu 开机参数

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机ID，示例：6520699837375
```

### 使用示例

```bash
acli vm advcfg machine-args get -v 6520699837375
```

### 结果示例

未设置时：

```bash
args:
vmID: 6520699837375
```

已设置时：

```bash
args: -no-hpet -nodefaults
vmID: 6520699837375
```