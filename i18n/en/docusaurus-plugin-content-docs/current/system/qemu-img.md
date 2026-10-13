---
sidebar_position: 1
---

# qemu-img

### Overview

Query disk image information and check image consistency (read-only, no repair).

### Command Parameters

This is a partially read-only command using a closed parameter whitelist (only listed parameters are allowed, others are rejected).

```bash
info <file>           Optional parameter. Query disk image information (read-only).
info -f <fmt> <file>  Optional parameter. Query disk image information with the specified format (read-only).
check <file>          Optional parameter. Check disk image consistency (read-only, no repair).
```

Write parameters (rejected on match):

```bash
create                Create a disk image (write)
convert               Convert disk image format (write)
resize                Resize a disk image (write)
commit                Commit disk image changes (write)
rebase                Change disk image backing file (write)
snapshot -c/-d/-a/-l  Create/delete/apply/list snapshots (write)
```

### Usage Example

```bash
acli system qemu-img info /sf/data/disk.qcow2
```

### Output Example

```bash
# acli system qemu-img info /sf/data/disk.qcow2
image: /sf/data/disk.qcow2
file format: qcow2
virtual size: 100 GiB (107374182400 bytes)
disk size: 12.5 GiB
cluster_size: 65536
Format specific information:
    compat: 1.1
    lazy refcounts: false
```