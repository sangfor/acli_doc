---
sidebar_position: 1
---

# uniq

### Overview

Filter and output adjacent duplicate lines from files or input streams, supporting piped input.

### Command Parameters

```bash
No parameters
```

This command supports passing parameters directly to the uniq command without parameter restrictions and can be used with pipes.

### Usage Example

```bash
acli system uniq /path/to/file
```

```bash
acli system uniq -c /path/to/file
```

### Output Example

```bash
# acli system uniq /data/app.log
line a
line b
line c
```
