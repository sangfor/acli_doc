---
sidebar_position: 1
---

# list

### Overview

Display deduplicated alerts of the current day

### Command Parameters

No parameters

### Usage Example

```bash
acli alert list
```

### Output Example

```bash
alert_type: sn_key_state_error
process: 100
object_type: Serial Number
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
type: Serial number KEY status abnormal
status: 2
description: Authorization USB key status abnormal. The serial number will automatically expire in 5 days. Please verify that the authorization USB key is properly inserted. If already inserted, promptly update the serial number on the authorization management page.
sysloged: 0
upid: null
unhandle_count: 36
host: 10.131.135.63
user: admin (10.131.135.63)
count: 36
hostid: host-005056893c9d
target: 10.131.135.63
log_id: host-005056893c9d:101139:1757378473:6875600288688
urgent_type: Emergency
otype: Serial Number
bcancel: 0
....
```