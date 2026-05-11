---
sidebar_position: 1
---

# get

### Overview

View system mounts information

### Command Parameters

No parameters
### Usage Example

```bash
acli system mounts get
```

### Output Example

```bash
acli system mounts get
/dev/sda3 / ext3 rw,noatime,nodiratime,nodioread_nolock,data=journal 0 0
tmpfs /var tmpfs rw,relatime,size=8388608k 0 0
tmpfs /etc tmpfs rw,relatime,size=524288k 0 0
tmpfs /sf/etc tmpfs rw,relatime,size=524288k 0 0
devtmpfs /dev devtmpfs rw,nosuid,size=32768k,nr_inodes=4352299,mode=755 0 0
...
```