---
sidebar_position: 1
---

# set

### Overview

Set data merge task configuration file merge_data.json content

### Command Parameters
```bash
-r|--running-interval=integer    Earliest trigger interval for startup data consolidation task, in seconds, for example: 60
-s|--stopped-interval=integer    Earliest trigger interval for shutdown data consolidation task, in seconds, for example: 60
-c|--cancel-interval=integer     Earliest trigger interval after canceling data consolidation task, in seconds, for example: 60
```

### Usage Example

```bash
acli platform backup datamover config set -r 60 --stopped-interval 1800
```

### Output Example

```bash
ok
```