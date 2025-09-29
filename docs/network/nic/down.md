---
sidebar_position: 10
---

# down
操作概述: 主机网口down

命令参数:
```bash
-h|--hostname 主机id
-n|--nic-name 网口名字
```

使用示例:
```bash
acli network nic down --hostname host-005056b2ec8d --nic-name eth2
```

结果示例:
```bash
task_id: UPID:host-005056b2ec8d:00009AFB:1ADD4A0:6874A955:编辑网口:10:admin@vtp:
```