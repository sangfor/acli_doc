---
sidebar_position: 3
---

# check_vm_model

### Overview

Check virtual machine business model

### Command Parameters

```bash
-v|--vmid=string               Required parameter, specify the VM ID to check, example: 6025407369236
-d|--monitorDataDir=string     Monitoring data directory, adding this option means analysis from monitoring files, otherwise real-time analysis, example: /tmp/
--lang=string                  Set the command line output language, options are zh_CN and en_US
-h|--help                      Display help information
```

### Usage Example

```bash
# Example 1: Check specified VM template (real-time analysis)
acli performance_tools check_vm_model -v 1649206016202

# Example 2: Check specified VM template (from monitoring file analysis)
acli performance_tools check_vm_model -v 1649206016202 -d /sf/data/local/monitor
```

### Output Example

```bash
Starting to get VM real-time data...
Starting to analyze VM data...
Failed to get memory load level, memory information is empty
VM disk average write speed: 0.00 MB/s, read speed: 0.00 MB/s, write latency: 0.00 ms, read latency: 0.22 ms, write block size: 0.00, read block size: 0.20, write queue depth: 0, read queue depth: 0.
VM network card average send rate: 0.00 MB/s, receive rate: 0.00 MB/s
VM CPU average usage: usr 0.65%, sys 0.47%, wait 0.05%, guest 0.35%, util 1.48%
Current VM model is: Low load type
Analysis recommendation: None
```
