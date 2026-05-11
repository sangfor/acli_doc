---
sidebar_position: 1
---

# ls

### Overview

Restrict access to files in the specified directory

### Command Parameters

No parameters
### Usage Example

```bash
acli system ls
```

### Output Example

```bash
Specify the absolute path parameter to view only files in the following directory:
/sf/cfg/
/sf/vs/vscfg/
/sf/data/
/run/
/var/
/sf/log/
/tmp/
/dev/

# acli system ls /var
30_vs_eth_check_temp.log
all.log
all.log.1
all.log.2
all.log.3
all.log.4
backups
bjdev_dvsport_notify
bond_fusion_preinit.log
cache
ce-status-monitor.lock
cfs_temp_file.list
cgroup_monitor_notify.backup
cgroup_monitor.sock
checkitem.sh.log
chkmntlog.log
clear_cache
```