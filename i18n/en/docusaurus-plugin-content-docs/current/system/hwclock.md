---
sidebar_position: 1
---

# hwclock

### Overview

Get hardware clock time

### Command Parameters

```bash
-r|--show=flag     Show RTC time (default behavior)
-v|--verbose=flag  Verbose output
--get=flag         Show RTC time with drift correction
-V|--version=flag  Show version information
```

### Usage Example

```bash
acli system hwclock -r
```

### Output Example

```bash
2026-09-09 10:07:03.992012+08:00
```
