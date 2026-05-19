---
sidebar_position: 3
---

# progress

### Overview

Query log collection task progress

### Command Parameters

```bash
No parameters (this command does not require parameters)
```

### Usage Example

```bash
acli log_collect progress
```

### Output Example

```bash
Status: Collection task completed!
Compressed file path (please manually delete the compressed file after downloading the log): /sf/data/local/private/123.zip
Overall progress: 100% - 1/1 (completed/total)
Total time: 00:00:46.3
10.131.136.156  Collection completed  100%
Log collection records:
  IP: 10.131.136.156
    x /sf/log/8.tar.gz
    x /sf/log/8.tar.zst
    x /sf/log/8.zst
    √ /sf/log/8/
    x /sf/log/blackbox/20260408.tar.gz
    x /sf/log/blackbox/20260408.zst
    √ /sf/log/blackbox/20260408/
    x /sf/log/vn-blackbox/20260408.tar.gz
    x /sf/log/vn-blackbox/20260408.zst
    √ /sf/log/vn-blackbox/20260408/
    x /boot/boot/log/install.log
    √ /boot/firmware/current/package/meta-inf/kernel_version
    √ /boot/firmware/current/package/meta-inf/version
    √ /boot/firmware/history
    x /boot/firmware/nvidia-vgpu-mgr/sgax-install.md5sum
    √ /cfs/
    √ /etc/hosts
    √ /sf/cfg/
    x /sf/data/local/kdump/*.kernel_core
    x /sf/data/local/sgax/md5file
    √ /sf/etc/
    √ /sf/kernel_version
    √ /sf/log/apache2/
    √ /sf/log/boot.log
    √ /sf/log/checkitem/
    √ /sf/log/compress_today_log.log
    √ /sf/log/containerd/
    x /sf/log/dump/
    √ /sf/log/host-agentd/
    x /sf/log/kdump/*.dmesg
    √ /sf/log/kernel_start.log
    √ /sf/log/kubelet/
    √ /sf/log/log_new.db
    √ /sf/log/mcelog.log
    x /sf/log/pstore/
    √ /sf/log/rd_rsync_check.log
    √ /sf/log/rd_switch_today_log.log
    √ /sf/log/sangfor_waf/
    √ /sf/log/sdn/
    √ /sf/log/sf-openapi/
    √ /sf/log/sfHCI_environment_init.log
    √ /sf/log/switch_today_log.log
    √ /sf/log/vtp/
    √ /sf/modules/loadmod.conf
    √ /sf/sgp/license/log/sf_license/
    √ /tmp/.alert.disk_dev.stat
    √ /tmp/.alert.host_mem_frequency.stat
    √ /tmp/.alert.sms_state.stat
    √ /tmp/.alert.vm_disk_dev.stat
    √ /tmp/drs/
    √ /tmp/hotplug_record
```
