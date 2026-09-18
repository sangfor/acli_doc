---
sidebar_position: 1
---

# get

### Overview

Get cluster system configuration

### Command Parameters

```bash
No parameters
```

### Usage Example

```bash
acli platform system_config get
```

### Output Example

```bash
{
  "compactmem_cpusage_limit": 70,
  "cpu_exclusive_type": 1,
  "cpusched_on_nodes": "",
  "defrag_method": 0,
  "encryption_algorithm": "aes_256",
  "hids_enable": 1,
  "host_gpu": 0,
  "if_cpusched_on": 0,
  "if_numa_on": 1,
  "keyboard": "en-us",
  "level_protect_enable": 0,
  "loop_speed": 0,
  "loop_timestream": "",
  "max_migration_concurrency_per_host": 2,
  "max_migration_concurrency_per_storage": 1,
  "sflsm_enable": 0,
  "show_component_vms_enable": 1,
  "single_endtime": "",
  "single_speed": 0,
  "single_starttime": "",
  "spdk_enable": 0,
  "suspended_enable": 1,
  "suspended_process": "no_process",
  "suspended_timeout": 2,
  "task_steal_enable": 0,
  "vcpu_type": "Cascadelake-Server-noTSX",
  "vgpu_mode": 0,
  "zta_mode": 2
}
```
