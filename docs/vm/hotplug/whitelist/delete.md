---
sidebar_position: 4
---

# delete

### 操作概述

删除指定OS的放通配置或关闭全局兜底

### 命令参数

```bash
-o|--os=string      可选参数，操作系统发行版标识(单个OS)，形如 <osname>,<位数>，示例：Ubuntu 14,64
-a|--all-unknown    可选参数，关闭全局兜底：还原为不支持未知OS的CPU/内存热添加，与 --os 互斥，示例：--all-unknown
```

### 使用示例

```bash
# 删除指定 OS 的放通配置
acli vm hotplug whitelist delete -o "Ubuntu 14,64"

# 关闭全局兜底
acli vm hotplug whitelist delete -a
```

### 结果示例

```bash
已删除 Ubuntu 14,64 的放通配置
```
