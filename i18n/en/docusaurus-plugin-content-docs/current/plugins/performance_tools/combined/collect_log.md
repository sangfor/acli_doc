---
sidebar_position: 1
---

# collect_log

### Overview

By virtual machine, automatically monitor virtual machines, automatically detect virtual machines and their host machines, and package related logs

### Command Parameters

```bash
-d|--date=string             Time to collect, defaults to now, format: 2006-01-02 15:04:05
--duration=integer           Log collection monitoring time for virtual machines, unit in minutes, default 5 minutes (default: 5)
--no-monitor                 Collect logs without monitoring virtual machines, default is to monitor
-v|--vmid=string             Required parameter, virtual machines to collect, example: 6025407369236
```

### Usage Example

```bash
# Example 1: Collect logs for specified virtual machine (using default monitoring time)
acli performance_tools combined collect_log -v 6025407369236

# Example 2: Collect logs for specified virtual machine (specify monitoring time)
acli performance_tools combined collect_log -v 6025407369236 --duration 10

# Example 3: Collect logs for specified time and virtual machine
acli performance_tools combined collect_log -v 6025407369236 -d "2025-06-25 10:30:00"

# Example 4: Collect logs for virtual machine without monitoring
acli performance_tools combined collect_log -v 6025407369236 --no-monitor
```

### Output Example

```bash
Starting to monitor virtual machine 6025407369236, time 1 minute
Starting to check virtual machine 6025407369236...
Starting to check host...
Starting to collect logs...
Starting to collect configuration files...
Starting to collect log files...
Starting to collect command outputs...
Starting to collect alert information...
Starting to collect operation logs...
Starting to compress folder: /sf/data/local/performance_tools/collect_log_v2_20260408_20260408
Packaging successful, file name: /sf/data/local/performance_tools/collect_log_v2_20260408_20260408.zip
```
