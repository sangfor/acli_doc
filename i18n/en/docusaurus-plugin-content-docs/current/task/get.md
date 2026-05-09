---
sidebar_position: 1
---

# get

### Overview

Query operation task information

### Command Parameters
```bash
-k|--keyword=string    Search the action, node, object, and description, Example: Login
-c|--code=string       Error code, When the --code parameter is used independently, the error code will be searched within tasks from the last 30 days by default. Example: 0x01002BB5
-v|--vm-id=string      VM ID, Example: 1223240430216
-t|--time=string       Specify time, Format: YYYY-MM-DD HH:MM:SS, YYYY-MM-DD HH
-H|--host=string       Specify the node, Example: host-005056b234ca
-s|--status=string     Specify the status, Enumeration values: progress, completed, failed, and queued, Enum values: progress,completed,failed,queued
-u|--upid=string       Asynchronous task UPID, Example: UPID:host-005056b2906f:0000AFC2:398B:6909A843:edit interface:1:admin@vtp:
-l|--limit=integer     Specify the number of records to display, such as 1 or 2, Default value: 50, Default: 50
```

### Usage Example

```bash
acli task get -H 'host-005056893c9d'
```

### Output Example

```bash
alert_type: Backup Report Data
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