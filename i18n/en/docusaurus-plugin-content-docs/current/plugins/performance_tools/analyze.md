---
sidebar_position: 6
---

# analyze

### Overview

Analyze log data to identify system and virtual machine bottlenecks

### Command Parameters

```bash
-d|--dir=string              Directory where log files are located (default: /sf/data/local/performance_tools/performance_data)
-s|--start=string            Log analysis start time, defaults to last 1 hour if not specified, format: 2006-01-02 15:04:05
-e|--end=string              Log analysis end time, defaults to last 1 hour if not specified, format: 2006-01-02 15:04:05
--lang=string                Set the command line output language, options are zh_CN and en_US
-h|--help                    Display help information
```

### Usage Example

```bash
# Example 1: Analyze log data from last 1 hour in default directory
acli performance_tools analyze

# Example 2: Analyze logs from specified time range
acli performance_tools analyze -s "2025-06-25 10:00:00" -e "2025-06-25 12:00:00"

# Example 3: Analyze logs from specified start time
acli performance_tools analyze -s "2025-06-25 10:00:00"

# Example 4: Analyze logs from specified directory
acli performance_tools analyze -d /tmp/performance_data

# Example 5: Combine specified directory and time range
acli performance_tools analyze -d /tmp/performance_data -s "2025-06-25 10:00:00" -e "2025-06-25 12:00:00"

# Example 6: Display help information
acli performance_tools analyze --help
```

### Output Example

```bash
Analyze log data to identify system and VM bottlenecks

Usage:
  performance_tools analyze [flags]

Flags:
  -d, --dir string     Directory where log files are located (default "/sf/data/local/performance_tools/performance_data")
  -e, --end string     Log analysis end time, defaults to last 1 hour if not specified, format: 2006-01-02 15:04:05
  -h, --help           help for analyze
  -s, --start string   Log analysis start time, defaults to last 1 hour if not specified, format: 2006-01-02 15:04:05

Global Flags:
      --lang string   Set the command line output language, options are zh_CN and en_US
```
