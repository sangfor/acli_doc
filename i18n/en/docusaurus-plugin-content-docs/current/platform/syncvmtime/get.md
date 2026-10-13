---
sidebar_position: 1
---

# get

### Overview

Get cluster VM time sync configuration

### Command Parameters

```bash
No parameters
```

### Usage Example

```bash
acli platform syncvmtime get
```

### Output Example

```bash
{
  "startup_sync_enable": 1,
  "timing_sync_enable": 0,
  "timing_sync_hw_clock": 1,
  "timing_sync_smooth": 0,
  "timing_sync_time_interval": 64,
  "timing_sync_tinker_panic": 0
}
```
