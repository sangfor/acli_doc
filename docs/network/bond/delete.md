---
sidebar_position: 10
---

# delete
操作概述: 删除聚合口

命令参数:
```bash
-h|--hostname=string                主机id，例如：host-005056b2a30a
-n|--bond-name=string               必要参数，聚合口名称，例如：channel1
```

使用示例:
```bash
acli network bond delete -n channel1
```

结果示例:
```bash
task_id: UPID:host-005056b234ca:0000ACFE:2758:68F8BEAB:删除聚合口:1:admin@vtp:
```