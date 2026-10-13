---
sidebar_position: 2
---

# restore

### Overview

Restore the low-latency parameter in grub.cfg

### Command Parameters

```bash
-p|--param=string    Required parameter, grub parameter name, enum: nohz_full (low-latency parameter)
```

### Usage Example

```bash
acli platform grub restore -p nohz_full
```

### Output Example

```bash
grub parameter restore operation succeeded
```
