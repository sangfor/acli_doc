---
sidebar_position: 1
---

# down

### 操作概述

禁用主机网口

### 命令参数

```bash
-n|--nic-name=string    必要参数，网口名字，示例：eth1
-h|--hostname=string    主机id，默认值，当前主机id，示例：host-005056893c9d
```

### 使用示例

```bash
acli network nic down --hostname host-005056b2ec8d --nic-name eth2
```

### 结果示例

```bash
task_id: UPID:host-005056b2ec8d:00009AFB:1ADD4A0:6874A955:编辑网口:10:admin@vtp:
```
