---
sidebar_position: 1
---

# precheck

### Overview

Check whether hosts in a virtual datastore support enabling the io_uring sqpoll feature

### Command Parameters

```bash
-v|--volume-id=string      Required parameter, volume id, example: a4ef106e_vs_vol_rep2
```

### Usage Example

```bash
acli storage asan io_uring sqpoll precheck -v a4ef106e_vs_vol_rep2
```

### Output Example

All checks passed:

```bash
sqpoll-precheck vol=a4ef106e_vs_vol_rep2                     STATUS: SUCCESS

  VOLUME CHECKS
    upgrade_in_progress  PASS
    volume_available     PASS
    volume_type          PASS

  host-002246213d6b                                                     PASS
  host-6c92bf51945a                                                     PASS
```

When some checks fail, the failing hosts are expanded check by check, and the blocking reason is listed under `BLOCKED BY`:

```bash
sqpoll-precheck vol=a4ef106e_vs_vol_rep2                      STATUS: FAILED

  VOLUME CHECKS
    upgrade_in_progress  PASS
    volume_available     PASS
    volume_type          FAIL

  host-002246213d6b                                                   FAILED
    sqpoll_storage_eligible  PASS
    tier_v2                  PASS
    kernel_version           FAIL
    legacy_libaio_engine     PASS
    host_maintain            PASS
    cache_disk_maintain      PASS
    nvme_cache_disk_count    PASS
    cpu_count                PASS
  host-6c92bf51945a                                                     PASS

  BLOCKED BY
    volume             volume_type     compound or non-blend volume is not supported
    host-002246213d6b  kernel_version  kernel version below 6.6
```

### Check Items

| Check | Level | Description |
| :---: | :---: | :--- |
| `upgrade_in_progress` | Volume | Enabling is not allowed while a cluster/patch upgrade is in progress |
| `volume_available` | Volume | The volume state must be available |
| `volume_type` | Volume | Compound volumes and non-hybrid volumes are not supported (an all-flash volume has no cache tier and needs no enabling) |
| `sqpoll_storage_eligible` | Host | All cache disks must be NVMe disks |
| `tier_v2` | Host | Tier v2 is not supported |
| `kernel_version` | Host | The kernel version must be 6.6 or later |
| `legacy_libaio_engine` | Host | The tier I/O engine must be cdev_iouring (cdev_aio is not allowed) |
| `host_maintain` | Host | The host must not be in maintenance mode |
| `cache_disk_maintain` | Host | Cache disks must not be in maintenance mode |
| `nvme_cache_disk_count` | Host | The number of NVMe cache disks must be 1 to 2 |
| `cpu_count` | Host | The number of logical cores must be at least 16 |