---
sidebar_position: 1
---

# asys

### Overview

Run the system check tool to detect the host

### Command Parameters

```bash
-s=string                (Required) Subcommand selection, enumerate values:
                              - offline (Check system offline status)
                              - all (Run all checks)
                              Special format: <command>:help Show detailed help for specific command, example: offline:dmesg
                                    - dmesg (Check dmesg log)
                                    - ipmi (Check IPMI log)
                                    - w3 (Check w3 scenario log)
-b=string                Begin time, format: YYYY-MM-DD HH:MM:SS, example: 2025-10-27 02:30
-e=string                End time, format: YYYY-MM-DD HH:MM:SS, example: 2025-10-27 12:30
-t=string                Date, format: YYYY-MM-DD, example: 2025-10-27 (Mutually exclusive with -b/-e, using -t automatically covers the full day)
-d=string                Only available in debug mode (-D), specify directory, example: /tmp.
                              Different behaviors based on different special formats in -s:
                                    - For dmesg, automatically discover dmesg suffix files, determine which dmesg to analyze based on time
                                    - For ipmi, default analyze ipmi log file ipmi.log
                                    - For w3, perform keyword analysis and timestamp analysis on all logs in the directory
-D|--debug               Enable debug mode
-c|--cmd_info            Show command information in JSON format
-h|--help                Show help information
-v|--version             Show version information
```

### Usage Examples

```bash
# Example 1: Show command help
acli asys -s offline:help

# Example 2: Check system offline status (specify time range)
acli asys -s offline -b "2025-10-27 02:30" -e "2025-10-27 12:30"

# Example 3: Check system offline status (specify date, automatically covers full day)
acli asys -s offline -t "2025-10-27"

# Example 4: Check dmesg log (specify time range)
acli asys -s offline:dmesg -b "2025-10-27 02" -e "2025-10-27 10"

# Example 5: Check dmesg log (specify date)
acli asys -s offline:dmesg -t "2025-10-27"

# Example 6: Check IPMI log (specify time range)
acli asys -s offline:ipmi -b "2025-10-27 06:30" -e "2025-10-27 18:30"

# Example 7: Check IPMI log (specify date)
acli asys -s offline:ipmi -t "2025-10-27"

# Example 8: Check w3 log (specify time range)
acli asys -s offline:w3 -b "2025-10-27 09" -e "2025-10-27 11"

# Example 9: Check w3 log (specify date)
acli asys -s offline:w3 -t "2025-10-27"

# Example 10: Run all checks
acli asys -s all -t "2025-10-27"
```

### Result Example

```bash
------------------------------------------------------
[asys] tool start running...
begin time must be specified
[asys] User params: s=offline:dmesg, b=2025-10-27 02, e=2025-10-27 10, t=, d=, D=false------------------------------------------------------
Tool Version: 1.1.60, Release Date: 2026-03-04
Executed Command: /sf/data/local/acli/plugins/asys/plugin -s offline:dmesg -b 2025-10-27 02 -e 2025-10-27 10
Current Date: 2026-04-08
If you need technical support, please collect logs and upload them to the log server using the following reference command:
acli log_collect create -s [ticket_id] -m offline -d [problem_date, e.g. YYYY-MM-DD]
[asys] Please collect Asys logs for further analysis: /sf/log/today/acli/plugin/acli_plugins_asys.log
------------------------------------------------------
```
