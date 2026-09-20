---
sidebar_position: 1
---

# get

### Overview

Get VS virtual storage volume details

### Command Parameters

```bash
-v|--volume-id=string   Virtual storage volume UUID, specify to output only that volume's details (standard 36-bit UUID format; when not specified, outputs all volumes). default=''
-p|--phy=string         Aggregate output by physical volume; merges the sub-volumes under the same physical volume (joined by '&'); when used together with --volume-id, the latter takes precedence, example: 1. default=''
```

### Usage Example

```bash
acli storage vsmgr volume get --volume-id <string> --phy <string>
```

### Output Example

```bash
[
    {
        "arbiter_info": {},
        "create_time": "2026-09-04 16:15:10",
        "data_hosts_num": 3,
        "data_storage_type": "ssd",
        "desc": "",
        "disks_num": 6,
        "fault_domain": [],
        "hosts": [
            "host-0050568ec35e",
            "host-0050568e74c8",
            "host-0050568e3fe4"
        ],
        "hosts_num": 3,
        "hosts_seq": [
            {"host_name": "host-0050568ec35e", "seq": 0},
            {"host_name": "host-0050568e74c8", "seq": 1},
            {"host_name": "host-0050568e3fe4", "seq": 2}
        ],
        "id": "8a83211f_vs_vol_rep3",
        "level": "server",
        "master": "host-0050568e3fe4",
        "name": "Virtual Datastore 1",
        "phy_vol_id": "8a83211f_vs_vol_rep3",
        "replica": 3,
        "replica_data_type": 4,
        "replica_type": 4,
        "status": "available",
        "storage_type": "ssd",
        "support_vhost": 1,
        "task": {
            "id": "bf6d96c2-a838-11f1-b755-0050568e81e1",
            "master": "host-0050568ec35e",
            "time": "2026-09-04 16:15:12",
            "type": "create_volume",
            "ver": 1
        },
        "task_two_host": 0,
        "topo_version": 3,
        "version": "7.0.0_B",
        "volume_type": "normal"
    }
]
```
