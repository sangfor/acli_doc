---
sidebar_position: 1
---

# get

### 操作概述

查询虚拟机指定网卡的自定义 qemu 开机参数

### 命令参数

```bash
-v|--vm-id=string     必要参数，虚拟机ID，示例：6520699837375
-n|--nic-id=string    必要参数，网卡ID，值为 iface_id，示例：f89a68a0-e44f-494b-9c52-7c47100cfddd（可用 vm advcfg nic-args list 获取）
```

### 使用示例

```bash
acli vm advcfg nic-args get -v 6520699837375 -n f89a68a0-e44f-494b-9c52-7c47100cfddd
```

### 结果示例

未设置时：

```bash
customArgs:
index: 0
nicID: f89a68a0-e44f-494b-9c52-7c47100cfddd
nicName: net0
vmID: 6520699837375
```

已设置时：

```bash
customArgs: mq=on,vectors=8
index: 0
nicID: f89a68a0-e44f-494b-9c52-7c47100cfddd
nicName: net0
vmID: 6520699837375
```