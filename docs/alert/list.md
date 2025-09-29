---
sidebar_position: 10
---

# list
操作概述: 从日志中搜索所有告警日志

命令参数:
```bash
无
```

使用示例:
```bash
acli alert list
```

结果示例:
```bash
alert_type: sn_key_state_error
process: 100
object_type: 序列号
pid:
vm:
mark_read: 0
id: 7287
reserved3: null
end: 1757378473
hostname: 10.131.135.63
object_id: host-005056893c9d
start: 2025-09-09 08:41:13
object_name: 10.131.135.63
type: 序列号KEY状态异常
status: 2
description: 授权USB-key状态异常，序列号将在5天后自动失效！请检查授权USB-key是否正确插入，如果已经插入，请及时在授权管理页面更新序列号！
sysloged: 0
upid: null
unhandle_count: 36
host: 10.131.135.63
user: admin (10.131.135.63)
count: 36
hostid: host-005056893c9d
target: 10.131.135.63
log_id: host-005056893c9d:101139:1757378473:6875600288688
urgent_type: 紧急
otype: 序列号
bcancel: 0
....
```