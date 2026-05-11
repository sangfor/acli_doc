---
sidebar_position: 1
---

# chping

### Overview

chping command

### Command Parameters

No parameters
### Usage Example

```bash
acli system chping
```

### Output Example

```bash
usage:
chping [options]

  options:

  -h                show this help text
  -c                package count, must > 0
  -s                package size, must > 0,  0, default is 1,000 msec
  -t                ttl, must > 0,  0, default is 5000,000 usec
  -l      set loglevel(0~12), bigger level get more log.
                    log will be printed on the screen when level is bigger than or equal to 12.
  destination
```