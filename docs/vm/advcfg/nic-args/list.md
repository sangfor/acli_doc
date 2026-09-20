---
sidebar_position: 1
---

# list

### 操作概述

列出虚拟机全部网卡及自定义 qemu 开机参数

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机ID，示例：6520699837375
```

### 使用示例

```bash
acli vm advcfg nic-args list -v 6520699837375
```

### 结果示例

```bash
nics:
  [0]:
    customArgs:
    index: 0
    nicID: f89a68a0-e44f-494b-9c52-7c47100cfddd
    nicName: net0
  [1]:
    customArgs:
    index: 1
    nicID: 3e35de83-cb2e-4ef8-80ad-c4c41ad550e3
    nicName: net1
vmID: 6520699837375
```