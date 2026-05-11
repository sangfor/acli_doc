---
sidebar_position: 1
---

# dump

### Overview

System memory usage

### Command Parameters

No parameters
### Usage Example

```bash
acli system memory dump
```

### Output Example

```bash
*MemAvailable:  23992 MB
*SwapTotal:     32767 MB
|- SwapFree:       32767 MB
|- SwapUsed:       0 MB
   |- SwapCached:     0 MB
*MemTotal:      39726 MB
|- Buffers:     897 MB
|- Cached:      5194 MB
   |- Clean:       4071 MB
   |- Dirty:       0 MB
   |- Shmem:       1123 MB
      |- VMvhost:     0 MB
|- Apps:        10091 MB
|- Qemu:        0 MB
|- HugePages:   652 MB
   |- HugePages_Free:   12 MB
   |- HugePages_Rsvd:   0 MB
|- VmallocUsed: 196 MB
|- Slab:        1457 MB
   |- SReclaimable:   1014 MB
   |- SUnreclaim:     442 MB
|- PageTables:  210 MB
|- KernelStack: 46 MB
|- MemFree:     19753 MB
|- HardwareCorrupted:   0 MB
|- Undefined:   1230 MB
```