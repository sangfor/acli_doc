---
sidebar_position: 1
---

# get

### 操作概述

查询告警信息

### 命令参数

```bash
-k|--keyword=string      搜索告警对象、事件和描述，示例：虚拟机异常挂起
-e|--event=string        指定事件，示例：免key序列号异常
-o|--object-name=string  指定告警对象，示例：10.134.244.34
-T|--object-type=string  指定告警对象类型，枚举值：host(主机),storage_obj(存储),vm(虚拟机),vnet(虚拟网络),sn(序列号),others(其他)
--starttime=string       指定告警起始时间，格式：'YYYY-MM-DD HH:MM:SS'、'YYYY-MM-DD HH'
--endtime=string         指定告警结束时间，格式：'YYYY-MM-DD HH:MM:SS'、'YYYY-MM-DD HH'
--distinct=integer       指定是否去重，枚举值：1（去重），0（不去重）
--mark_read=string       指定标记已读的告警ID，多个ID用英文逗号分隔，示例：1,2,3
--start=integer          指定从第几条记录开始展示，默认值为0
-L|--level=integer       指定级别，枚举值：1（紧急），0（普通）
-l|--limit=integer       指定展示记录的数目（默认值为50），示例：1，2等
```

### 使用示例

```bash
acli alert get -o '10.131.135.63'
```

### 结果示例

```bash
alert_type: vs_mongo_host_state
process: 100
object_type: 存储
pid:
vm:
mark_read: 0
id: 7355
reserved3: null
end: 1757418712
hostname: 10.131.135.63
object_id: 10.131.135.63
start: 2025-09-09 19:51:52
object_name: 10.131.135.63
type: 存储服务异常
status: 2
description: 检测到主机<10.131.135.63>的虚拟存储集群服务异常，请联系深信服科技处理。
sysloged: 0
upid: null
host: 10.131.135.63
user: admin (10.131.135.63)
hostid: host-005056893c9d
target: 10.131.135.63
log_id: host-005056893c9d:54836:1757418712:4142550845026
urgent_type: 紧急
otype: 存储
bcancel: 0
....
```
