---
sidebar_position: 1
---

# get

### 操作概述

查询组播配置

### 命令参数

```bash
-e|--evs-id      物理出口ID，示例：16f0fa33-9d4f-49b8-b855-65a176b8283d
```

### 使用示例

```bash
acli network anet multicast get --evs-id 16f0fa33-9d4f-49b8-b855-65a176b8283d
```

### 结果示例

```bash
evswitches:
  [0]:
    deleted: 0
    deleted_at: null
    description:
    id: 16f0fa33-9d4f-49b8-b855-65a176b8283d
    mcst_enable: 1
    mcst_filtering_mode: snooping
    mcst_unknown_drop_enable: 1
    name: test11
    revision_number: 1
    tenant_id: 707e9d9dac814227b90941362efb6616
```
