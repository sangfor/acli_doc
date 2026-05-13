---
sidebar_position: 1
---

# set

### Overview

Update loadman service configuration

### Command Parameters
```bash
-e|--enabled=integer          Required parameter, Whether to enable overload protection, enumeration values: 0(disable), 1(enable), Enum values: 0,1
-c|--cpu-threshold=integer    Required parameter, CPU threshold percentage, range 70-98
```

### Usage Example

```bash
acli service asv loadman config set -e 1 -c 90
```

### Output Example

```bash
cpu_threshold: 90
enabled: 1
```