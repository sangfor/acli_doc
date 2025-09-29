---
sidebar_position: 10
---

# list
操作概述: 获取所有硬盘信息

命令参数:
```bash
无
```

使用示例:
```bash
acli storage asan disk list
```

结果示例:
```bash
total: 4
   disk_number:
      disk_num_arbiter: 0
      disk_num_none: 0
      disk_num_cache: 0
      disk_num_data: 4
      disk_num_backup: 0
      disk_num_total: 4
   disks:
      ssd_life: -
      fault_list:
      ip: 10.131.135.63
      iostat:
         is_update_lv_total: 1
         io_write_rate: 0
         io_read_rate: 0
         disk_pvs_size: 214748364800
         disk_pvs_free_size: 176999628800
         mtime: 1754300996.52507
         io_write_count: 0
         io_await: 0
         io_read_count: 0
      iops_ok: 1
      storage_type: STORAGE_DATA
      disk: 005056893c9d_36000c29463c9fad7a55fafde714b0031
      light_on: 0
      replaced_disk:
      warn_info:
      disk_alias: 6000c29463c9fad7a55fafde714b0031 VMware Virtual disk
      read_ok: 1
      used_size: 25165824000
      disk_sn: 6000c29463c9fad7a55fafde714b0031 VMware Virtual disk
      status: NORMAL
      used: 140509184
      disk_dump: 0
      major_fault: NONE
      alert:
      volume_id: a4ef106e_vs_vol_rep2
      disk_type: DISK_SSD
      disk_name: 6000c29463c9fad7a55fafde714b0031 VMware Virtual disk
      disk_size: 214748364800
      fault: NONE
      dev: /dev/sdd
      disk_location:
      life_ok: 1
      host_name: host-005056893c9d
      volume_name: 虚拟存储卷1
      disk_group_id: 2
  ......
```