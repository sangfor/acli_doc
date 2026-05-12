---
sidebar_position: 1
---

# get

### Overview

Get maintenance information related to overload protection

### Command Parameters
```bash
-s|--status=flag                View overload protection status, CPULevel, and isolated core count from redis
-b|--boot-process=flag          View initial process information of loadman startup
-c|--cgroup-information=flag    View cgroup information
-p|--parameter=flag             View loadman service startup parameters
```

### Usage Example

```bash
acli service asv loadman maintenance get -b
```

### Output Example

```bash
3109603
```