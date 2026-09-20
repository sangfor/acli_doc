---
sidebar_position: 1
---

# list

### Overview

List backup pool storage

### Command Parameters

```bash
-b|--backup=integer              Whether to show only backup pool storage. 1=only backup pools, 0=only non-backup pools. enum=[0, 1]
-s|--samba=integer               Whether to show shared directories (samba). 1=show, 0=hide. enum=[0, 1]
-q|--query=string                Fuzzy match pattern for storage name filtering (case-insensitive), example: nfs
-l|--lt256g-not-display=integer  Whether to hide disks smaller than 256G. 1=hide, 0=show. default=1 enum=[0, 1]
-S|--s3-not-display=integer      Whether to hide S3 storage. 1=hide, 0=show. default=0 enum=[0, 1]
```

### Usage Example

```bash
acli storage backuppool list
acli storage backuppool list --backup 1 --samba 1
```

### Output Example

```bash
{
  "data": [
    {
      "backup_total": 0,
      "backup_used": 1048576,
      "enable": 0,
      "name": "lv_1788498920",
      "status": 1,
      "storage": "36000c295d99e6f3fa5cbecdd69ab905b_0050568e74c8",
      "type": "local",
      "usable": 1
    },
    {
      "backup_total": 0,
      "backup_used": 4096,
      "enable": 0,
      "name": "Virtual Datastore 1",
      "nfstype": "vsnfs",
      "status": 1,
      "storage": "8a83211f_vs_vol_rep3",
      "type": "vsnfs",
      "usable": 1
    },
    {
      "backup_total": 0,
      "backup_used": 1048576,
      "enable": 0,
      "name": "lv_1788505284",
      "status": 1,
      "storage": "36000c29314cd19d551b5fa23ceadd85a_0050568ec35e",
      "type": "local",
      "usable": 1
    },
    {
      "backup_total": 0,
      "backup_used": 1048576,
      "enable": 0,
      "name": "lv_1788505226",
      "status": 1,
      "storage": "36000c29e4768b003a742abc581f351e3_0050568e3fe4",
      "type": "local",
      "usable": 1
    }
  ]
}
```
