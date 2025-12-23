---
sidebar_position: 10
---

# get
操作概述: 显示指定cgroup的所有参数信息

命令参数:
```bash
-g|--group=string  需要显示的cgroup控制器及路径，示例：memory:/monopoly
```

使用示例:
```bash
acli system cgroup get -g cpuset:/
```

结果示例:
```bash
/:
cpuset.preferred_cpus: 
cpuset.memory_pressure: 0
cpuset.memory_migrate: 0
cpuset.memory_pressure_enabled: 0
cpuset.mem_exclusive: 1
cpuset.memory_spread_slab: 0
cpuset.cpu_exclusive: 1
cpuset.effective_mems: 0
cpuset.effective_cpus: 0-7
cpuset.sched_load_balance: 1
cpuset.mems: 0
cpuset.mem_hardwall: 0
cpuset.sched_relax_domain_level: -1
cpuset.cpus: 0-7
cpuset.memory_spread_page: 0
```