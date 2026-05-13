---
sidebar_position: 1
---

# list

### 操作概述

展示虚拟机锁列表

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机id，示例：1268314679221
```

### 使用示例

```bash
acli vm lock list -v 1268314679221
```

### 结果示例

```bash
[0]:
  filePath: /cfs/vm_tmp_status/flag_dir/2987661685263.saga.lock
  lockKey: 2987661685263.saga.lock
  lockPath:
  runID:
  sagaStatus:
  vmid: 1268314679221
```
