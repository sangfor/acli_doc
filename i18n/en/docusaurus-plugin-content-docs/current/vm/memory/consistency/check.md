---
sidebar_position: 1
---

# check

### Overview

Check memory consistency, compare memory configuration (MB) across DB, CFS, and Qemu

### Command Parameters

```bash
-v|--vm-id=string    Required parameter, VM ID. Example: 614182240912
```

### Usage Example

```bash
# Check memory consistency
acli vm memory consistency check -v 614182240912
```

### Output Example

```bash
{"VMID":"614182240912","MemoryMB":{"DBValue":"4096","CfsValue":"4096","QemuValue":"2048","Consistent":false},"CheckTime":"2026-05-26T11:18:07+08:00","Status":"inconsistent"}
```