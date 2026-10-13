---
sidebar_position: 3
---

# status

### Overview

Show the status of the low-latency parameter in grub.cfg

### Command Parameters

```bash
-p|--param=string    Required parameter, grub parameter name, enum: nohz_full (low-latency parameter)
```

### Usage Example

```bash
acli platform grub status -p nohz_full
```

### Output Example

```bash
=== nohz_full status ===
current grub.cfg nohz_full=    : 2-3
state file                     : /sf/etc/grub_ctl/nohz_full.state
  saved fingerprint            : 5.10.0-1_xxx
  current fingerprint          : 5.10.0-1_xxx
  fingerprint changed          : no
  saved value                  : 2-3
  saved action                 : removed
```
