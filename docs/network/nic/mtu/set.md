---
sidebar_position: 10
---

# set
操作概述: 设置网口mtu

命令参数:
```bash
-h|--hostname=string                主机id，例如：host-005056b2a30a
-n|--nic-name=string                必要参数，网口名称
-m|--mtu=string                     必要参数，mtu

```

使用示例:
```bash
acli network nic mtu set --hostname host-005056b2ec8d --nic-name eth4 --mtu 1600
```

结果示例:
```bash
task_id: UPID:host-005056b2ec8d:00009AFB:1ADD4A0:68774DFC:编辑网口:20:admin@vtp:
```
