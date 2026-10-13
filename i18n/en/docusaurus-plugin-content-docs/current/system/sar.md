---
sidebar_position: 1
---

# sar

### Overview

Collect and view system activity reports (CPU, memory, IO, etc., read-only).

### Command Parameters

This is a partially read-only command; options are not whitelisted (allowed by default), but the blacklisted parameters below are rejected on match.

Forbidden parameters (rejected on match):

```bash
-o <file>  Writes binary data to a file (write operation). Rejected.
```

### Usage Example

```bash
acli system sar -u 1 5
```

### Output Example

```bash
# acli system sar -u 1 5
Linux 4.18.0-193.el8.x86_64 (hostname)    2026-09-08

10:20:01     CPU     %user     %nice   %system   %iowait    %steal     %idle
10:20:02     all      2.50      0.00      1.00      0.00      0.00     96.50
10:20:03     all      3.00      0.00      0.50      0.00      0.00     96.50
Average:     all      2.75      0.00      0.75      0.00      0.00     96.50
```
