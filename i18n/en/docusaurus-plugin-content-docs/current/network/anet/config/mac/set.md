---
sidebar_position: 1
---

# set

### Overview

Adjust the capacity of the mac table

### Command Parameters
```bash
-l|--learn-limit=integer    Required parameter, Mac table capacity specifications, 51000(min), 262144(max), Enum values: 51000,262144
```

### Usage Example

```bash
acli network anet config mac set -l 262144
```

### Output Example

```bash
Command executed successfully.
```