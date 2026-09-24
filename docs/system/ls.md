---
sidebar_position: 1
---

# ls

### 操作概述

列出白名单内指定目录下的文件

### 命令参数

本命令为既有命令的路径白名单扩展，仅允许列出白名单内的路径。

```bash
<path>  必要参数，指定要列出的目录，仅允许白名单内的路径，示例：/var/log/
```

可列出的路径白名单（ls 命令族共用：ls/du/df/md5sum/find 目录列举/校验族，去包含后 40 条，节选）：

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

### 使用示例

```bash
acli system ls /var/log/
```

### 结果示例

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
