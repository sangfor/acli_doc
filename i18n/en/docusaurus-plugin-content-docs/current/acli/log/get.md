---
sidebar_position: 1
---

# get

### Overview

Display logs of the aCLI tool

### Command Parameters
```bash
-c|--context=integer    Number of output context lines, Example: 2
-p|--pattern=string     Regular expression, Example: err*
-d|--date=string        Specify the log date, Format: YYYY-MM-DD
-l|--level=string       Display logs of a specified level, Enumeration values: debug, info, warning, error, critical, Enum values: debug,info,warning,error,critical
```

### Usage Example

```bash
# Query Debug-Level Log Information
acli acli log get -l debug
```

### Output Example

```bash
2025-03-21 10:34:22 [DEBUG] Starting acli command execution
2025-03-21 10:34:23 [INFO] Command executed successfully
2025-03-21 10:34:24 [WARNING] Potential performance issue detected
```