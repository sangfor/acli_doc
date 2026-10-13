---
sidebar_position: 1
---

# remove

### Overview

Remove the low-latency parameter from grub.cfg

### Command Parameters

```bash
-p|--param=string    Required parameter, grub parameter name, enum: nohz_full (low-latency parameter)
```

### Usage Example

```bash
acli platform grub remove -p nohz_full
```

### Output Example

```bash
grub parameter remove operation succeeded
```
