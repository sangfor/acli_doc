---
sidebar_position: 1
---

# parse

### Overview

Parse cgroup black-box logs

### Command Parameters
```bash
-f|--file=string      Specify the cgroup black-box log file, default: /sf/log/blackbox/today/LOG_cgroup,txt
-g|--group=string     Required parameter, Cgroup controllers and paths to show,format: <cgroup_controller>:<cgroup_path>, example: memory:/monopoly
-p|--params=string    Required parameter, Specify the parameter names to query, separated by commas, Parameters can include the controller prefix or omit it. Example: memory.usage_in_bytes, limit_in_bytes
```

### Usage Example

```bash
acli log cgroup parse -g cpuset:/management -p cpus,preferred_cpus,mems
```

### Output Example

```bash
25-12-23 16:40:00
  cpus: 4-7
  mems: 0
25-12-23 16:40:59
  cpus: 4-7
  mems: 0
25-12-23 16:42:00
  cpus: 4-7
  mems: 0
25-12-23 16:43:00
  cpus: 4-7
  mems: 0
25-12-23 16:44:00
  cpus: 4-7
  mems: 0
25-12-23 16:45:01
  cpus: 4-7
  mems: 0
25-12-23 16:46:01
  cpus: 4-7
  mems: 0
25-12-23 16:47:02
  cpus: 4-7
  mems: 0
25-12-23 16:48:02
  cpus: 4-7
  mems: 0
25-12-23 16:49:03
  cpus: 4-7
  mems: 0
25-12-23 16:50:03
  cpus: 4-7
  mems: 0
25-12-23 16:51:04
  cpus: 4-7
  mems: 0
25-12-23 16:52:04
  cpus: 4-7
  mems: 0
```