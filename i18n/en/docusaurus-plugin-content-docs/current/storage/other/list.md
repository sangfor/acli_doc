---
sidebar_position: 1
---

# list

### Overview

Display a list of storage information, excluding virtual storage

### Command Parameters
```bash
-v|--vsnfs=integer                 If this parameter is set to 1, NFS storage will be displayed, Default value: 1. Enumeration values: 0, 1, Enum values: 0,1
-L|--lt256g-not-display=integer    If this parameter is set to 1, disks smaller than 256 GB will not be displayed, Default value: 1. Enumeration values: 0, 1, Default: 1
-q|--query=string                  Filter storage by name (case-insensitive, fuzzy match)
-s|--start=integer                 The first entry on the storage list, This parameter must be used together with the --limit parameter. Example: --start 0 --limit 10, which indicates that 10 entries will be returned, starting from entry 0.
-l|--limit=integer                 The maximum number of entries in the storage list, to be used with the --start parameter, Example: --start 0 --limit 10, which indicates that 10 entries will be returned, starting from entry 0.
-t|--lv-type=string                Datastore type, Enumeration values: local, iscsi, fc, nfs, s3. By default, this parameter is not specified, and all datastore types are displayed., Enum values: local,iscsi,fc,nfs,s3
```

### Usage Example

```bash
# Filter Storage, Return Only the First 10 Local Storage Records
acli storage other list -v 1 -L 1 -s 0 -l 10 -t local
```

### Output Example

```bash
s3:
iscsi:
fc:
nfs:
virtual_storage:
local:
  active_host: host-0050568949a9
  maxwrite: 330139136
  used_ratio: 15.58
  urgent: 0
  total: 317827579904
  id: 36000c29922b9c9311483578fab141e6c_0050568949a9
  write_cnt: 43
  host_cnt: 1/1
  avail: 268298092544
  read_cnt: 1
  shared: 0
  nodes: host-0050568949a9
  type: local
  running_vms: 1
  status: 1
  read_ratio: 512
  used: 49529487360
  alert: 0
  disable: 0
  active: 1
  name: lv_1749527550
  maxread: 347384320
  active_host_name: 10.131.139.53
  hosts: 1
  ats: -1
  discard: 0
  write_ratio: 1076736

  active_host: host-005056893b01
  maxwrite: 406502912
  used_ratio: 0.10
  urgent: 0
  total: 317827579904
  id: 36000c293cadee3074f68ee64716b4163_005056893b01
  write_cnt: 0
  host_cnt: 1/1
  avail: 317521395712
  read_cnt: 0
  shared: 0
  nodes: host-005056893b01
  type: local
  running_vms: 0
  status: 1
  read_ratio: 0
  used: 306184192
  alert: 0
  disable: 0
  active: 1
  name: lv_1749527551
  maxread: 175596544
  active_host_name: 10.131.139.51
  hosts: 1
  ats: -1
  discard: 0
  write_ratio: 0
nof:
```