---
sidebar_position: 1
---

# date

### Overview

date command, used to get the current system time (read-only).

### Command Parameters

```bash
-d|--date=string  Optional parameter. Display the time described by the given string. Example: acli system date -d "2025-08-27"
-u|--utc=flag     Optional parameter. Display the time in UTC. Example: acli system date -u
+<format>         Optional parameter. Output using the given format. Example: acli system date +%Y-%m-%d
```

Forbidden parameters (rejected on match, including GNU unique-prefix abbreviations):

```bash
-f|--file=string  Forbidden. Reads date lines from a file (batch mode), a file read operation. Rejected.
                  Because GNU getopt accepts unique-prefix abbreviations, any form starting with --f
                  (--f / --fi / --fil) is also rejected. date has no other long option starting with f,
                  so --f is its shortest unique prefix.
```

### Usage Example

```bash
acli system date
```

### Output Example

```bash
Wed Aug 27 14:23:52 GMT-8 2025
```