---
sidebar_position: 1
---

# check

### 操作概述

检测CPU一致性，对比数据库、CFS 和 Qemu 的 CPU 插槽数、每插槽核心数和总vCPU数

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机ID，示例：614182240912
```

### 使用示例

```bash
# 检测CPU一致性
acli vm cpu consistency check -v 614182240912
```

### 结果示例

```bash
{"VMID":"614182240912","Sockets":{"DBValue":"1","CfsValue":"1","QemuValue":"","Consistent":true},"CoresPerSocket":{"DBValue":"1","CfsValue":"1","QemuValue":"","Consistent":true},"TotalVCPUs":{"DBValue":"1","CfsValue":"1","QemuValue":"1","Consistent":true},"CheckTime":"2026-05-26T11:18:46+08:00","Status":"consistent"}
```
