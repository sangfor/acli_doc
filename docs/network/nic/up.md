---
sidebar_position: 1
---

# up

### 操作概述

启用主机网口

### 命令参数

```bash
-n|--nic-name=string    必要参数，网口名字，示例：eth1
-h|--hostname=string    主机id，示例：host-005056893c9d
```

### 使用示例

```bash
acli network nic up --hostname host-005056b2ec8d --nic-name eth2
```

### 结果示例

```bash
task_id: UPID:host-005056b2ec8d:00009AFB:1ADD4A0:6874A804:编辑网口:6:admin@vtp:
```
