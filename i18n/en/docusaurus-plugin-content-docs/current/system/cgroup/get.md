---
sidebar_position: 1
---

# get

### Overview

Display all parameter information for the specified cgroup

### Command Parameters
```bash
-g|--group=string           Required parameter, Control group which info should be displaye, example: memory:/monopoly
```

### Usage Example

```bash
acli system cgroup get -g cpuset:/
```

### Output Example

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