---
sidebar_position: 10
---

# list
操作概述: 列出cgroup下cpu空间内的所有文件

命令参数:
```bash
无
```

使用示例:
```bash
acli system cgroup cpu list
```

结果示例:
```bash
asan
cgroup.clone_children
cgroup.procs
cgroup.sane_behavior
compute
cpuacct.stat
cpuacct.usage
cpuacct.usage_all
cpuacct.usage_percpu
cpuacct.usage_percpu_sys
cpuacct.usage_percpu_user
cpuacct.usage_sys
cpuacct.usage_user
cpu.cfs_period_us
cpu.cfs_quota_us
```