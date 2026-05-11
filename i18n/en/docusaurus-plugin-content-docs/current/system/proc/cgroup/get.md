---
sidebar_position: 1
---

# get

### Overview

Get the cgroup information for the specified process

### Command Parameters
```bash
-p|--pid=integer            Required parameter, Process ID, example: 122063
```

### Usage Example

```bash
acli system proc cgroup get -p 1
```

### Output Example

```bash
14:misc:/
13:freezer:/init.scope
12:pids:/init.scope
11:cpuset:/
10:hugetlb:/
9:devices:/init.scope
8:memory:/init.scope
7:net_cls,net_prio:/
6:files:/
5:blkio:/init.scope
4:perf_event:/
3:cpu,cpuacct:/init.scope
2:rdma:/
1:name=systemd:/init.scope
```