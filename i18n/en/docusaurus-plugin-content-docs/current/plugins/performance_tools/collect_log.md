---
sidebar_position: 5
---

# collect_log

### Overview

Collect host performance related logs, configurations, command execution results

### Command Parameters

```bash
-s|--start=string             Log collection start date, defaults to today, format: 2006-01-02
-e|--end=string               Log collection end date, defaults to same as start date, format: 2006-01-02
-o|--output=string            Folder where queried logs are stored, default location is: /sf/data/local/performance_tools
-t|--type=string              Specify the data types to collect, optional values:
                                - config (configuration files)
                                - log (log files)
                                - command (command outputs)
                                - alert (alert information)
                                - oplog (operation logs)
                              Multiple types separated by commas, default collect all
-v|--vmids=string             Specify specific virtual machines, multiple VMs separated by commas, example: 6025407369236
-g|--generate-config          Generate default configuration for log collection
--lang=string                 Set the command line output language, options are zh_CN and en_US
-h|--help                     Display help information
```

### Usage Example

```bash
# Example 1: Collect logs for specified date range
acli performance_tools collect_log -s 2025-06-25 -e 2025-06-27

# Example 2: Collect logs for specified date
acli performance_tools collect_log -s 2025-06-25

# Example 3: Only collect configuration files
acli performance_tools collect_log -t config

# Example 4: Collect multiple types of logs
acli performance_tools collect_log -t config,log,command

# Example 5: Specify output directory
acli performance_tools collect_log -o /tmp/performance_logs

# Example 6: Specify specific virtual machine
acli performance_tools collect_log -v 6025407369236

# Example 7: Specify multiple virtual machines
acli performance_tools collect_log -v 6025407369236,6025407369237

# Example 8: Combine multiple parameters
acli performance_tools collect_log -s 2025-06-25 -e 2025-06-27 -t config,log -v 6025407369236 -o /tmp/performance_logs

# Example 9: Generate default configuration
acli performance_tools collect_log -g
```

### Output Example

```bash
Starting to collect configuration files...
Starting to compress folder: /sf/data/local/performance_tools/collect_log_v2_20260408_20260408
Packaging successful, file name: /sf/data/local/performance_tools/collect_log_v2_20260408_20260408.zip
```
