---
sidebar_position: 1
---

# slabtop

### Overview

Display kernel slab cache object counts, utilization, and memory usage.

### Command Parameters

Command format:

```bash
acli system slabtop [options]
```

Supported parameters:

This command uses a closed allowlist for read-only options. Only the listed options are permitted; other options are rejected.

```text
-o|--once=flag      Display once and exit
-h|--help=flag      Show help information
-V|--version=flag   Show version information
-d|--delay=integer  Set the refresh interval in seconds, range: 1-3600
-s|--sort=string    Set the sort character; only one of a, b, c, l, v, n, o, p, s, u is allowed
```

Forbidden arguments:

Reject unlisted options, refresh intervals outside 1-3600, and sort characters outside `[abclvnopsu]`.

### Usage Example

```bash
acli system slabtop -o
```

### Output Example

```text
slabtop: terminal setting retrieval: Inappropriate ioctl for device
 Active / Total Objects (% used)    : 4210648 / 4268922 (98.6%)
 Active / Total Slabs (% used)      : 113531 / 113531 (100.0%)
 Active / Total Caches (% used)     : 129 / 175 (73.7%)
 Active / Total Size (% used)       : 1220027.33K / 1251331.38K (97.5%)
 Minimum / Average / Maximum Object : 0.01K / 0.29K / 9.06K

  OBJS ACTIVE  USE OBJ SIZE  SLABS OBJ/SLAB CACHE SIZE NAME
1032966 1031980  99%    0.21K  27918       37    223344K dentry
602990 598447  99%    0.02K   3547      170     14188K lsm_file_cache
556832 556822  99%    0.12K  17401       32     69604K buffer_head
332552 332552 100%    0.70K  15116       22    241856K inode_cache
205044 205044 100%    0.14K   7323       28     29292K kernfs_node_cache
157696 157457  99%    0.01K    308      512      1232K kmalloc-8
137344 130136  94%    0.06K   2146       64      8584K anon_vma_chain
134160 133223  99%    0.77K   6708       20    107328K proc_inode_cache
103872 103026  99%    1.00K   3246       32    103872K kmalloc-1k
 88026  82841  94%    0.04K    863      102      3452K vma_lock
 87061  82498  94%    0.21K   2353       37     18824K vm_area_struct
 76025  75058  98%    0.31K   3041       25     24328K skbuff_head_cache
 65178  65178 100%    0.04K    639      102      2556K extent_status
 60956  60850  99%    0.57K   2177       28     34832K radix_tree_node
 59520  59265  99%    0.03K    465      128      1860K kmalloc-32
 54976  54976 100%    0.50K   1718       32     27488K pool_workqueue
```

The first line reports a terminal settings retrieval issue; this output still includes the subsequent slab statistics.
