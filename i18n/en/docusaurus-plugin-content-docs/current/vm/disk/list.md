---
sidebar_position: 1
---

# list

### Overview

Display the disk image list of the target VM

### Command Parameters
```bash
-v|--vm-id=string           Required parameter, VM ID, Example: 3535177259949
```

### Usage Example

```bash
acli vm disk list -v 2749923911666
```

### Output Example

```bash
total 131076
-rw-r--r-- 1 root root      1241 Aug  5 07:11 4872898137715.conf
-rw------- 1 root root 134217728 Jul 29 17:11 vm-disk-1.qcow2
```