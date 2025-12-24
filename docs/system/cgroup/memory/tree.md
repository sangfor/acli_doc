---
sidebar_position: 10
---

# tree
操作概述: 显示内存cgroup子系统的子组结构

命令参数:
```bash
无
```

使用示例:
```bash
acli system cgroup memory tree
```

结果示例:
```bash
/mnt/cgroup/memory {used: 14.161606, limit: -1, pids: 576} (Unit: GB)

init.scope  {used: 0.016239, limit: -1, pids: 1}
k8s.io  {used: 0.026325, limit: -1}
│    # Dismissed subgroups (41 subgroups)
monopoly  {used: 20.421543, limit: -1}
├─ hugepage_group  {used: 0.0, limit: 0.636719}
├─ noncore_group  {used: 20.421543, limit: 35.052414, pids: 339}
│  └─ monopoly  {used: 4.109211, limit: -1}
│     ├─ kernel_group  {used: 0.0, limit: 12.5}
│     ├─ network_compute_group  {used: 4.109211, limit: 10.177414, pids: 72}
│     │  ├─ monopoly  {used: 0.523106, limit: -1}
│     │  │  └─ network_group  {used: 0.523106, cache_to: share/compute_root_group, limit: -1, pids: 13}
│     │  └─ share  {used: 0.779636, limit: 5.177414}
│     │     ├─ command_sandbox_group  {used: 0.003716, limit: 15.0}
│     │     │  └─ share  {used: 0.0, limit: -1}
│     │     │     └─ command_sandbox_migrate_group  {used: 0.0, limit: 4.0}
│     │     └─ compute_root_group  {used: 0.775921, oom_control: 1 (OOM killer disabled), limit: -1}
│     │        └─ share  {used: 0.0, limit: -1}
│     │           ├─ important_compute_group  {used: 0.0, oom_control: 1 (OOM killer disabled), limit: -1}
│     │           └─ normal_compute_group  {used: 0.0, oom_control: 1 (OOM killer disabled), limit: -1}
│     ├─ normal_service_group  {used: 0.0, limit: 5.0}
│     └─ vs_service_group  {used: 0.0, limit: 7.375}
└─ system_service_group  {used: 0.0, limit: 3.0}
share  {used: 0.0, limit: 0.0}
sys-fs-fuse-connections.mount  {used: 0.0, limit: -1}
sys-kernel-config.mount  {used: 0.0, limit: -1}
sys-kernel-debug.mount  {used: 0.0, limit: -1}
sys-kernel-tracing.mount  {used: 0.0, limit: -1}
system.slice  {used: 0.462357, limit: -1}
│    # Dismissed subgroups (29 subgroups)
user.slice  {used: 0.0, limit: -1}
```