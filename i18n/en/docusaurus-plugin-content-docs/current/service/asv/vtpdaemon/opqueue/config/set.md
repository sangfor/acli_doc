---
sidebar_position: 1
---

# set

### Overview

Set process op queue config

### Command Parameters
```bash
-w|--work=integer             Maximum number of tasks in the process op queue, example: 13
-W|--wait=integer             Maximum wait number of the process op queue, example: 1000
-p|--pressure-work=integer    Maximum number of tasks in the process op pressure queue, value range 0-9999, example: 4
```

### Usage Example

```bash
acli service asv vtpdaemon opqueue config set -w 14 -W 999
```

### Output Example

```bash
Normal case:
OK
```