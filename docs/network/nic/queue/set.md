---
sidebar_position: 10
---

# set
操作概述: 设置网口队列数

命令参数:
```bash
-h|--hostname=string 主机id，默认值，当前主机id，示例：host-005056893c9d
-n|--nic-name=string 网口名字，示例：eth1
-c|--ring-count=string 发送和接收的队列数，json格式字符串，示例：'{"current": 8}'
```

使用示例:
```bash
acli network nic queue set --nic-name eth4 --ring-count '{"current": 8}'
```

结果示例:
```bash
task_id: UPID:host-005056b2a30a:00009FD5:3B5A:68F72FB5:编辑网口:20:admin@vtp:
```
