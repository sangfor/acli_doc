---
sidebar_position: 1
---

# restart

### 操作概述

重启rrdcached服务

### 命令参数

无参数

### 使用示例

```bash
acli service asv rrdcached restart
```

### 结果示例
```bash
acli service asv rrdcached restart

    Already stoped: rrdcached
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Prerun (pidof rrdcached >/dev/null || rm -f /var/run/rrdcached.pid ; /sf/bin/pre_rrdcached_start.sh) return: 1 ... (warning).
Start (/usr/bin/rrdcached -l unix:/var/run/vtp-datareport-rrdcached.sock -F -b /sf/data/datareport_database/rrd -B -z 540 -w 600 -V LOG_INFO -p /var/run/rrdcached.pid) OK! 4125899.
```
