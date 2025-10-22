---
sidebar_position: 10
---

# set
操作概述: 设置当前网口环形缓冲区参数

命令参数:
```bash
-h|--hostname=string 主机id，默认值，当前主机id，示例：host-005056893c9d
-n|--nic-name=string 网口名字，示例：eth1
-c|--ring-buffer=string 设置当前网口环形缓冲区参数，json格式字符串，示例：'{"current": {"rx": 4096, "tx": 4096}}'
```

使用示例:
```bash
acli network nic ring set --nic-name eth4 --ring-buffer '{"current": {"rx": 4096, "tx": 4096}}'
```

结果示例:
```bash
task_id: UPID:host-005056b2a30a:00009FD5:3B5A:68F732C6:编辑网口:28:admin@vtp:
```
