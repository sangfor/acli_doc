---
sidebar_position: 1
---

# list

### 操作概述

查询 VS 虚拟存储卷列表

### 命令参数

```bash
无参数
```

### 使用示例

```bash
acli storage vs_status volume list
```

### 结果示例

```bash
{
  "data_ready": 1,
  "fail": [],
  "volumes": [
    {
      "alerts": [
        {
          "context": "检测到主机<10.131.137.124>的网口<eth5>存在丢包，请检查该主机网口的网线或者网口跟交换机的兼容性。",
          "status": "warn"
        },
        {
          "context": "检测到主机<10.131.136.197>的网口<eth5>存在丢包，请检查该主机网口的网线或者网口跟交换机的兼容性。",
          "status": "warn"
        },
        {
          "context": "检测到主机<10.131.137.114>的网口<eth5>存在丢包，请检查该主机网口的网线或者网口跟交换机的兼容性。",
          "status": "warn"
        }
      ],
      "cache_capacity_ratio": 0,
      "data_host_num": 3,
      "dedup_comp_enable": 0,
      "dedup_comp_stat": {
        "after_dedup_comp_size": 0,
        "before_dedup_comp_size": 0,
        "compress_rate": 1,
        "dedup_comp_rate": 1,
        "dedup_rate": 1,
        "distribute_save_rate": 0,
        "distribute_save_size": 0,
        "is_high_dedup_comp_rate": false,
        "space_save_rate": 0,
        "volume_origin_use_size": 0,
        "volume_real_use_size": 0
      },
      "disk_num": 6,
      "disk_num_cache": 0,
      "fail_size": 0,
      "features": [
        {
          "name": "rdma",
          "switch": "off"
        }
      ],
      "free": 2065812160512,
      "free_disk_num": 0,
      "free_rate": 99,
      "hdd_disk_num": 0,
      "health_status": "warn",
      "host_num": 3,
      "id": "8a83211f_vs_vol_rep3",
      "io_read": 0,
      "io_write": 0,
      "master_risk_status": 0,
      "name": "虚拟存储卷1",
      "replica": 3,
      "replica2": 1032906080256,
      "replica3": 688597762048,
      "ssd_disk_num": 6,
      "storage_type": "ssd",
      "total": 2065849909248,
      "used": 37748736,
      "vm_num": 1,
      "vms_running": 0,
      "volume_status": "available",
      "volume_type": "ssd"
    }
  ]
}
```
