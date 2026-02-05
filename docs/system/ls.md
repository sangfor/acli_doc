---
sidebar_position: 1
---

# ls

### 操作概述

ls命令

### 命令参数

无参数

### 使用示例

```bash
acli system ls
```

### 结果示例

```bash
请指定绝对路径参数，仅能查看如下目录下的文件：
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
