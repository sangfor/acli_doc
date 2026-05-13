---
sidebar_position: 1
---

# restart

### Overview

Restart the rrdcached service

### Command Parameters

No parameters

### Usage Example

```bash
acli service asv rrdcached restart
```

### Output Example
```bash
acli service asv rrdcached restart

    Already stoped: rrdcached
 Physical cores /dev/null || rm -f /var/run/rrdcached.pid ; /sf/bin/pre_rrdcached_start.sh) return: 1 ... (warning).
Start (/usr/bin/rrdcached -l unix:/var/run/vtp-datareport-rrdcached.sock -F -b /sf/data/datareport_database/rrd -B -z 540 -w 600 -V LOG_INFO -p /var/run/rrdcached.pid) OK! 4125899.
```