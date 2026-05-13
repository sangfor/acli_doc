---
sidebar_position: 1
---

# get

### Overview

Obtain loadman service configuration

### Command Parameters

No parameters

### Usage Example

```bash
acli service asv loadman config get
```

### Output Example

```bash
cpu_threshold: 90
enabled: 1
master_cores: 2
controller_cores: 4
compute_cores: 8
```

Note: The return values of `master_cores`, `controller_cores`, and `compute_cores` are non-negative integers. A return value of `0` indicates that the corresponding node type uses the system default value.
