---
sidebar_position: 1
---

# find

### Overview

Search for files in a specified directory by criteria (read-only).

### Command Parameters

This is a partially read-only command using a closed parameter whitelist (only listed parameters are allowed, others are rejected).

```bash
<path>            Required parameter. Specify the search starting directory (only paths in the ls command family path whitelist are allowed). Example: /sf/data/
-name <pattern>   Match by file name (case-sensitive)
-iname <pattern>  Match by file name (case-insensitive)
-type <type>      Filter by file type (f/d/l/b/c/p/s)
-size <size>      Filter by file size
-mtime <n>        Filter by modification time (days)
-mmin <n>         Filter by modification time (minutes)
-atime <n>        Filter by access time (days)
-ctime <n>        Filter by status change time (days)
-maxdepth <n>     Maximum search depth
-mindepth <n>     Minimum search depth
-print            Print matching results (default)
-print0           Print matching results separated by null
-ls               Print matching results in ls format
-path <pattern>   Match by full path
-perm <mode>      Filter by permission bits
-user <name>      Filter by owner
-group <name>     Filter by group
-newer <file>     Newer than the specified file
-fstype <type>    Filter by file system type
```

Path whitelist (shared by the ls command family: ls/du/df/md5sum/find directory-list/validation family; 40 entries after redundancy removal; excerpt):

```bash
/boot/
/cfs/
/sf/data/
/sf/log/
/sys/class/net/
/run/
```

Write parameters (rejected on match):

```bash
-exec    Executes commands on find results (write). Rejected.
-delete  Deletes matching files (write). Rejected.
-ok      Interactively executes commands on find results (write). Rejected.
```

### Usage Example

```bash
acli system find /sf/log/ -name "*error*" -type f
```

### Output Example

```bash
# acli system find /sf/log/ -name "*error*" -type f
/sf/log/error.log
/sf/log/error.2026-09-08.log
```
