---
sidebar_position: 10
---

# up
操作概述: 主机网口up

命令参数:
```bash
-h|--hostname 主机id
-n|--nic-name 网口名字
```

使用示例:
```bash
acli network nic up --hostname host-005056b2ec8d --nic-name eth2
```

结果示例:
```bash
task_id: UPID:host-005056b2ec8d:00009AFB:1ADD4A0:6874A804:编辑网口:6:admin@vtp:
```