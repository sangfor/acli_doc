---
sidebar_position: 1
---

# list

### Overview

List VS virtual storage volumes

### Command Parameters

```bash
No parameters
```

### Usage Example

```bash
acli storage vs_status volume list
```

### Output Example

```bash
{
  "data_ready": 1,
  "fail": [],
  "volumes": [
    {
      "alerts": [
        {
          "context": "Packet loss occurs on the node(10.131.137.124)'s interface(eth5). Please check whether network cable is well plugged or whether the interface is compatible with switch.",
          "status": "warn"
        },
        {
          "context": "Packet loss occurs on the node(10.131.136.197)'s interface(eth5). Please check whether network cable is well plugged or whether the interface is compatible with switch.",
          "status": "warn"
        },
        {
          "context": "Packet loss occurs on the node(10.131.137.114)'s interface(eth5). Please check whether network cable is well plugged or whether the interface is compatible with switch.",
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
      "name": "Virtual Datastore 1",
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
