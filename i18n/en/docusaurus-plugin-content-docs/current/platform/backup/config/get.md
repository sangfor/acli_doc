---
sidebar_position: 1
---

# get

### Overview

Get the content of the backup task configuration

### Command Parameters
```bash
No parameters
```

### Usage Example

```bash
acli platform backup config get
```

### Output Example

```bash
{
  "agentless_backup_task": 16,
  "agentless_backup_task_max": 128,
  "agentless_backup_task_min": 2,
  "agentless_disk_resource_task": 16,
  "agentless_disk_resource_task_max": 128,
  "agentless_disk_resource_task_min": 2,
  "auto_speed": 1,
  "backup_cmk_recycle_seconds": 1814400,
  "backup_io_queue_max_concurrency": "2",
  "backup_job_speed": 52428800,
  "backup_speed": "839909376",
  "backup_speed_limit_connection": 800,
  "backup_speed_limit_connection_max": 9900,
  "backup_speed_limit_connection_min": 8,
  "backup_speed_limit_host": 800,
  "backup_speed_limit_host_max": 100000,
  "backup_speed_limit_host_min": 0,
  "block_stream_status": {},
  "cdp_io_queue_max_concurrency": 2,
  "delete_speed": "52428800",
  "healthcheck_host_limited_task": 2,
  "healthcheck_speed": "41943040",
  "healthcheck_storage_limited_task": "3",
  "is_separate": 1,
  "limited_speed": "314572800",
  "limited_task": "3",
  "max_backup_copy_task": "4",
  "max_backup_io_queue_max_concurrency": 8,
  "max_backup_speed": 1258291200,
  "max_delete_speed": 268435457,
  "max_s3_capacity": 109951162777600,
  "max_s3_num_limit": 2,
  "max_storage_delete_task_count": 16,
  "max_storage_task_count": 16,
  "min_backup_io_queue_max_concurrency": 1,
  "min_backup_speed": 2,
  "min_delete_speed": 1,
  "min_s3_capacity": 274877906944,
  "min_storage_delete_task_count": 1,
  "min_storage_task_count": 1,
  "network_interface": {},
  "num_coroutines": 8,
  "read_co_num": 4,
  "read_merge_cluster": 4,
  "snapshot_merge_speed": 83886080,
  "snapshot_merge_speed_max": 314572300,
  "snapshot_merge_speed_min": 0,
  "storage_task_limit": 9,
  "storage_task_limit_max": 256,
  "storage_task_limit_min": 2,
  "write_merge_num": 4
}

```