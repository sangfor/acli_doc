---
sidebar_position: 1
---

# md5sum

### Overview

Calculate the MD5 checksum of a specified file (read-only).

### Command Parameters

No parameters

Parameter and path validation notes: `--files0-from=<file>` specifies the list file of the files to hash; that list file itself must be in the ls command family path whitelist, and positional arguments (the files to hash) must also be in the ls command family path whitelist. Because GNU getopt accepts unique-prefix abbreviations, abbreviated forms such as `--fi <file>` are recognized in the same way and validated by the same rule, so they cannot bypass the path whitelist check.

Path whitelist (shared by the ls command family: ls/du/df/md5sum/find directory-list/validation family; 40 entries after redundancy removal; excerpt):

```bash
/boot/
/cfs/
/sf/data/
/sf/log/
/sys/class/net/
/run/
```

See the shared path whitelist of the ls command family for the complete list.

### Usage Example

```bash
acli system md5sum /sf/version
```

### Output Example

```bash
# acli system md5sum /sf/version
d41d8cd98f00b204e9800998ecf8427e  /sf/version
```
