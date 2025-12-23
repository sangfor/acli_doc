---
sidebar_position: 10
---

# get
操作概述: 获取指定进程的cgroup信息

命令参数:
```bash
-p|--pid=integer    进程号，示例：122063
```

使用示例:
```bash
acli system proc cgroup get -p 1
```

结果示例:
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