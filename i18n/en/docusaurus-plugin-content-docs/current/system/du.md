---
sidebar_position: 1
---

# du

### Overview

Estimate the disk space usage of the specified directory or file (read-only).

### Command Parameters

This is a partially read-only command; options are not whitelisted (allowed by default), but the blacklisted parameters below are rejected on match. At most 1 positional argument is accepted, and its path must be in the shared path whitelist of the ls command family.

Forbidden parameters (rejected on match, including GNU unique-prefix abbreviations):

```bash
--files0-from=<file>  Reads the list of paths to measure from a file (file read operation). Rejected.
                      Because GNU getopt accepts unique-prefix abbreviations, any form starting
                      with --f (--f / --fi / --fil / --files0) is also rejected.
```

Measurable path whitelist (shared by the ls command family: ls/du/df/md5sum/find directory-list/validation family; 40 entries after redundancy removal; excerpt):

```bash
/boot/
/cfs/
/dev/
/etc/netplan/
/etc/sysconfig/network-scripts/
/lib/modules/
/mnt/cgroup/cpu
/run/
/sf/data/
/sf/log/
/sys/class/net/
/var/
```

### Usage Example

```bash
acli system du /sf/data/
```

### Output Example

```bash
# acli system du /sf/data/
6144    /sf/data/local/mock/mc/mc0
1024    /sf/data/local/mock/mc/mc1/dimm2
1024    /sf/data/local/mock/mc/mc1/dimm1
2048    /sf/data/local/mock/mc/mc1/dimm0
5120    /sf/data/local/mock/mc/mc1
12288   /sf/data/local/mock/mc
20480   /sf/data/local/mock
```