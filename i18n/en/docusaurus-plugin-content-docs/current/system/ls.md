---
sidebar_position: 1
---

# ls

### Overview

List files in the specified directory within the whitelist.

### Command Parameters

This is an existing command extended with a path whitelist. Only whitelisted paths can be listed.

```bash
<path>  Required parameter: specify the directory to list. Only whitelisted paths are allowed. Example: /var/log/
```

Listable path whitelist (shared by the ls command family: ls/du/df/md5sum/find directory-list/validation family; 40 entries after redundancy removal; excerpt):

```bash
/boot/
/cfs/
/dev/vd*
/etc/netplan/
/etc/sysconfig/network-scripts/
/lib/modules/
/mnt/cgroup/cpu
/mnt/shared/qemu_vhost_user/setpci
/run/
/sf/bin/ovftool/ovftool.bin
/sf/data/
/sf/etc/overload_mode
/sf/log/
/sys/class/net/
/var/crash/
/var/log/dp/
```

### Usage Example

```bash
acli system ls /var/log/
```

### Output Example

```bash
# acli system ls /var/log/
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
```
