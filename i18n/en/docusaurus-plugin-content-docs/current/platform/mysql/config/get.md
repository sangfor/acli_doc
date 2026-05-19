---
sidebar_position: 1
---

# get

### Overview

Get MySQL configuration

### Command Parameters

No parameters

### Usage Example

```bash
acli platform mysql config get
```

### Output Example

```bash
# CHKVER:3# ***DO NOT EDIT FIRST LINE***
[mysqld]
server-id                    = 1
max_connections              = 750
rpl_semi_sync_slave_enabled  = ON
rpl_semi_sync_master_enabled = ON
super_read_only              = 0
read_only                    = 0
report_host                  = host-005056893c9d
```