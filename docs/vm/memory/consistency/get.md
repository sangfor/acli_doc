---
sidebar_position: 1
---

# get

### 操作概述

获取内存一致性状态，对比数据库、CFS 和 Qemu 的内存配置（MB）

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机ID，示例：614182240912
```

### 使用示例

```bash
acli vm memory consistency get -v 614182240912
```

### 结果示例

```bash
{"VMID":"614182240912","MemoryMB":{"DBValue":"4096","CfsValue":"4096","QemuValue":"2048","Consistent":false},"CheckTime":"2026-05-26T11:18:07+08:00","Status":"inconsistent"}
```