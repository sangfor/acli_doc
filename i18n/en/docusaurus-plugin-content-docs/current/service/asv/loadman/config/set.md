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
-m|--master-cores=integer     Optional parameter, Non-negative integer. Isolated CPU cores on cluster controller. Default: 0, Maximum: 80% of the node's total CPU cores
--controller-cores=integer    Optional parameter, Non-negative integer. Isolated CPU cores on controller node. Default: 0, Maximum: 80% of the node's total CPU cores
--compute-cores=integer       Optional parameter, Non-negative integer. Isolated CPU cores on compute node. Default: 0, Maximum: 80% of the node's total CPU cores
```

### Usage Example

```bash
acli service asv loadman config set -e 1 -c 90 -m 2 --controller-cores 4 --compute-cores 8

acli service asv loadman config set -e 1 -c 90 -m 2
```

### Output Example

```bash
cpu_threshold: 90
enabled: 1
master_cores: 2
controller_cores: 4
compute_cores: 8
```
