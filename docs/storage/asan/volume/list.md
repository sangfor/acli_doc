---
sidebar_position: 10
---

# list
操作概述: 获取卷列表

命令参数:
```bash
无
```

使用示例:
```bash
acli storage asan volume list
```

结果示例:
```bash
fail:
data_ready: 1
volumes:
  disk_num: 4
  features:
     switch: off
     name: rdma
  replica2: 655819276288
  storage_type: ssd
  replica: 2
  io_read: 0
  total: 1311923765248
  id: a4ef106e_vs_vol_rep2
  dedup_comp_stat:
     distribute_save_size: 0
     is_high_dedup_comp_rate: false
     before_dedup_comp_size: 0
     after_dedup_comp_size: 0
     volume_origin_use_size: 0
     compress_rate: 1
     dedup_rate: 1
     dedup_comp_rate: 1
     space_save_rate: 0
     distribute_save_rate: 0
     volume_real_use_size: 0
  disk_num_cache: 0
  io_write: 0
  cache_capacity_ratio: 0
  data_host_num: 2
  host_num: 2
  used: 285212672
  free_rate: 99
  free: 1311638552576
  fail_size: 0
  vms_running: 1
  free_disk_num: 0
  name: 虚拟存储卷1
  master_risk_status: 0
  volume_type: ssd
  hdd_disk_num: 0
  health_status: ok
  ssd_disk_num: 4
  volume_status: available
  dedup_comp_enable: 0
  vm_num: 1
```