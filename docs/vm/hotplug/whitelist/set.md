---
sidebar_position: 3
---

# set

### 操作概述

修改指定OS的CPU/内存热添加放通能力

### 命令参数

```bash
-o|--os=string        必要参数，操作系统发行版标识(单个OS)，形如 <osname>,<位数>，示例：Ubuntu 14,64
-c|--cpu=boolean      可选参数，CPU热添加能力，true/false；需先指定 --os 使用（--os 为必填），未传入保持原值，示例：true
-m|--memory=boolean   可选参数，内存热添加能力，true/false；需先指定 --os 使用（--os 为必填），未传入保持原值，示例：false
```

### 使用示例

```bash
# 修改指定 OS 的 CPU 热添加能力
acli vm hotplug whitelist set -o "Ubuntu 14,64" -c true

# 修改指定 OS 的内存热添加能力
acli vm hotplug whitelist set -o "Ubuntu 14,64" -m false

# 同时修改 CPU 与内存热添加能力
acli vm hotplug whitelist set -o "Ubuntu 14,64" -c true -m true
```

### 结果示例

```bash
已修改 Ubuntu 14,64：CPU热添加 支持
```
