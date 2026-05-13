---
sidebar_position: 1
---

# dump

### Overview

Display CBT file content in hexadecimal format

### Command Parameters
```bash
-f|--filename=string    Required parameter, Absolute path of the disk file, for example: /sf/xxx/vm-disk-1,qcow2
-s|--start=integer      Starting offset (optional, default is 0), for example: 0
-l|--length=integer     Dump length (optional, if not specified, dump all data from start to end of file), for example: 1024
```

### Usage Example

```bash
acli platform backup cbt file dump -f="/sf/data/36000c299bd876efc9d30909bec1d556b_0050569b7e33/disks/08/57/019b4ef9-f7cd-7cdf-bee1-08571ac1ddd1/019b4ef9-f7cd-7cdf-bee1-08571ac1ddd1.qcow2" -s 0 --length 1024
```

### Output Example

```bash
cbt file path: /sf/data/36000c299bd876efc9d30909bec1d556b_0050569b7e33/disks/08/57/019b4ef9-f7cd-7cdf-bee1-08571ac1ddd1/019b4ef9-f7cd-7cdf-bee1-08571ac1ddd1.qcow2.cbt.version
version_id: 1
inc_id: 16
checkpoint_id: 4294967312
granularity: 65536 bytes
cluster_count: 3276800 
disk_size: 214748364800 bytes
data_crc: 4294967295, it is not reset
header_crc: 3686558728
0000000000000000         3 
```