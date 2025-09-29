---
sidebar_position: 10
---

# get
操作概述: 从操作日志中搜索指定关键字的操作日志

命令参数:
```bash
-k|--key-word=string  搜索行为、主机、对象和描述
-c|--code=string      错误码，比如0x01002BB5
-t|--time=string      指定时间，格式：'YYYY-MM-DD HH:MM:SS'、'YYYY-MM-DD HH'
-H|--host=string      指定主机，比如host-005056b234ca
-s|--status=integer   指定状态，枚举值，1（进行中），100（完成），-1（失败），-2（排队中）
-l|--limit=integer    指定展示记录的数目，（默认值为50），比如1，2等
```

使用示例:
```bash
acli task get -H 'host-005056893c9d'
```

结果示例:
```bash
alert_type: 备份报表数据
process: Failed
object_type:
pid:
vm:
id: 172
reserved3:
dest_host:
sched_effect:
end: 1757406086
event_id: 53084160
hostname: 10.131.135.63
object_id:
start: 2025-09-09 16:21:26
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
log_id: host-005056893c9d:125938:1757406086:6302466651181
errcode_tracing: 0x01002386/0x0100028A/0x01000AD8/0x01000AD8/0x01000AD8/0x01000AD8
ha_handle_action:
otype: host
bcancel: 0
action_type: 10
request_id: ,8bfe04947cb6b9ff281edcd0b9baffe5
....
```