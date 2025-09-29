---
sidebar_position: 10
---

# list
操作概述: 从操作日志中列出所有操作日志

命令参数:
```bash
无
```

使用示例:
```bash
acli task list
```

结果示例:
```bash
alert_type: 备份报表数据
process: Failed
object_type:
pid:
vm:
id: 170
reserved3:
dest_host:
sched_effect:
end: 1757377415
event_id: 53084160
hostname: 10.131.135.63
object_id:
start: 2025-09-09 08:23:35
object_name:
sched_reason:
ha_handle_result:
type: Back up report data
status: 3
description: The cluster controller (10.131.135.63) failed to back up report data to another controller node (host-00505689470b), which may result in report data loss. Please contact a technical support representative.
sysloged: 0
upid:
host: 10.131.135.63
module_type: 50
user: admin (10.131.135.63)
risk_level: 10
hostid: host-005056893c9d
target: 10.131.135.63
log_id: host-005056893c9d:126008:1757377415:4342539117592
errcode_tracing: 0x01002386/0x0100028A/0x01000AD8/0x01000AD8/0x01000AD8/0x01000AD8/0x01000C27
ha_handle_action:
otype: host
bcancel: 0
action_type: 10
request_id: ,8bf6fc665138088dd99e7c43054911f3
....
```