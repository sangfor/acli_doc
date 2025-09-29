---
sidebar_position: 10
---

# get
操作概述: 查看节点信息

命令参数:
```bash
-n|--node-name=string 节点名称
```

使用示例:
```bash
acli platform node get --node-name 10.131.201.84
```

结果示例:
```bash
10.131.201.84
   ip: 10.131.201.84
   id: host-005056b2a994
   master: 0
   status: 1
   alert: 0
   controller: 1
   controller_pool: 1
   name: 10.131.201.84
```