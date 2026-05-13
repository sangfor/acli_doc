---
sidebar_position: 1
---

# iostat

### Overview

Obtain iostat information of virtual datastore

### Command Parameters
```bash
-v|--volume-id=string     Required parameter, Datastore ID, Example: a4ef106e_vs_vol_rep2
-t|--time-frame=string    Required parameter, Obtain the required time length, Enumeration values: hour, day, week, custom
-S|--storage=integer      To update storage capacity changes, set this parameter to 1, Default value: 1. Enumeration values: 0, 1, Enum values: 0,1, Default: 1
-h|--hitrate=integer      To update the hit rate trend, set the parameter to 1, Default value: 1. Enumeration values: 0, 1, Default: 1
-s|--start=string         Custom start time, to be used with the --time-frame parameter set to custom, Example: 2025-12-12 12:12:12
-e|--end=string           Custom end time, to be used with the --time-frame parameter set to custom, Example: 2025-12-12 02:12:12
```

### Usage Example

```bash
acli storage asan volume iostat -v a4ef106e_vs_vol_rep2 -t custom -S 1 -h 1 -s '2025-12-12 12:12:12' -e '2025-12-12 14:12:12'
```

### Output Example

```bash
host_hitrate_sheet:
  series:
  start_time: 0
  interval: 0
  end_time: 0
  unit: %
throughput_sheet:
  series:
     data:
name: I/O Read Data Volume

     data:
name: IO Write Data Volume
  start_time: 1765512735
  interval: 5
  end_time: 1754301690
  unit: Bps
storage_sheet:
  series:
     data: 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1311921668096, 1311919570944, 1311919570944, 1311919570944, 1311918522368, 1311638552576, 1311638552576, 1311638552576, 1311638552576, 1311638552576
name: Idle capacity

     data: 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2097152, 4194304, 4194304, 4194304, 5242880, 285212672, 285212672, 285212672, 285212672, 285212672
name: Used Capacity

     data: 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
name: Failed capacity
  start_time: 1749166620
  interval: 86400
  end_time: 1754264220
  unit: B
latency_sheet:
  series:
     data:
name: I/O read latency

     data:
name: I/O write latency
  start_time: 1765512735
  interval: 5
  end_time: 1754301690
unit: millisecond
vol_hitrate_sheet:
  series:
     data:
name: Cache Hit Rate
  start_time: 0
  interval: 0
  end_time: 0
  unit: %
iops_sheet:
  series:
     data:
name: IO read count

     data:
name: IO write count
  start_time: 1765512735
  interval: 5
  end_time: 1754301690
unit: times/second or per second
```