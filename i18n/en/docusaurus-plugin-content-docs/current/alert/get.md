---
sidebar_position: 1
---

# get

### Overview

Query alert information

### Command Parameters
```bash
-k|--keyword=string        Search the alert object, event, and description, Example: VM suspended unexpectedly
-e|--event=string          Specify the event, Example: Virtual license key anomaly
-o|--object-name=string    Specify the alert object, Example: 10.134.244.34
-T|--object-type=string    Specify the alert object type, Enumeration values: host (Node), storage_obj (Storage), vm (VM), vnet (Virtual Network), sn (Serial Number), others (Others)., Enum values: host,storage_obj,vm,vnet,sn,others
-t|--time=string           Specify time, Format: YYYY-MM-DD HH:MM:SS, YYYY-MM-DD HH
-L|--level=integer         Specify the level, Enumeration values: 1 (Critical), 0 (Noncritical), Enum values: 0,1
-l|--limit=integer         Specify the number of records to display, such as 1 or 2, Default value: 50, Default: 50
```

### Usage Example

```bash
acli alert get -o '10.131.135.63'
```

### Output Example

```bash
alert_type: vs_mongo_host_state
process: 100
object_type: Storage
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
type: Storage Service Exception
status: 2
description: An anomaly has been detected in the virtual storage cluster service on host . Please contact Sangfor Technologies for assistance.
sysloged: 0
upid: null
host: 10.131.135.63
user: admin (10.131.135.63)
hostid: host-005056893c9d
target: 10.131.135.63
log_id: host-005056893c9d:54836:1757418712:4142550845026
urgent_type: Emergency
otype: Storage
bcancel: 0
....
```