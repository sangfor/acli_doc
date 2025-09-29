---
sidebar_position: 10
---

# get
操作概述: 根据虚拟机id获得虚拟机配置

命令参数:
```bash
-v|--vm-id=string  虚拟机的ID，示例：1072335336316
```

使用示例:
```bash
acli vm config get -v 1072335336316
```

结果示例:
```bash
abnormal_recovery: 1
balloon_memory: 0
boot: cdn
bootdisk: ide0
cfgstorage: a4ef106e_vs_vol_rep2
compatibility_version: vmx_version=vmx-3.14,src_hci_version=6.10.0_R2
cores: 8
cpu: core2duo
cpu_exclusive: 0
cpu_reserve: 0
create_time: 1755572365
disable_ple: 0
enable_network_affinity: 0
encrypted: 0
file_filter: 0
graphic_type: cirrus
ha_enable: 1
high_performance_disks: ide0
host: cluster
host_gpu: 0
hotplug: 3
hugepage: 0
ide0: a4ef106e_vs_vol_rep2:vm-disk-1.qcow2,cache=real_directsync,preallocate=off,forecast=disable,cache_size=256,volume_type=qcow2,unmap=off,size=120G
....
```