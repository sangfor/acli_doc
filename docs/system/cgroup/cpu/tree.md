---
sidebar_position: 10
---

# tree
操作概述: 显示cpu cgroup子系统的子组结构

命令参数:
```bash
无
```

使用示例:
```bash
acli system cgroup cpu tree
```

结果示例:
```bash
# Subsystem mount points: /sys/fs/cgroup/cpuset,/sys/fs/cgroup/cpu,cpuacct,/sys/fs/cgroup/cpu,cpuacct

/mnt/cgroup/cpu {aff_low_pct: -1, cpu_exclusive: True, mem_exclusive: True, shares: 1024, mems: 0, usage: 1525272.26s, cpus: 0-7, quota: -1}

compute [share]  {aff_low_pct: -1, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 0.00s}
init.scope  {aff_low_pct: -1, shares: 1024, usage: 117.67s, quota: -1}
k8s.io  {aff_low_pct: -1, shares: 1024, usage: 436.93s, quota: -1}
│    # Dismissed subgroups (41 subgroups)
management [part_monopoly]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 890468.79s}
├─ strict [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 854134.51s}
│  ├─ high [share]  {aff_low_pct: 70, cpus: 4-7, shares: 2048, quota: -1, mems: 0, usage: 577337.15s}
│  │  ├─ adesk [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 238.22s}
│  │  ├─ anet [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 86668.97s}
│  │  ├─ asan [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 210708.95s}
│  │  ├─ asv [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 248593.51s}
│  │  │  ├─ cmdproxy-server_stat_tmp  {usage: 815.24s, aff_low_pct: -1, quota: -1, shares: 1024}
│  │  │  │     # ERROR: In subsystems 'cpuset' not find this cgroup
│  │  │  │     # WARNING: Not found in mgmt runtime file, directly create cgroup is fobiden !!!
│  │  │  └─ zookeeper [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: 125000, mems: 0, usage: 4606.04s}
│  │  │     # INFO: cpu.cfs_period_us, 250000 is not default value 100000
│  │  ├─ bdr [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 720.71s}
│  │  ├─ compute [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 16506.32s}
│  │  ├─ ops [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 2078.94s}
│  │  └─ system [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 3777.19s}
│  ├─ low [share]  {aff_low_pct: 70, cpus: 4-7, shares: 512, quota: -1, mems: 0, usage: 127407.57s}
│  │  ├─ adesk [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 0.00s}
│  │  ├─ anet [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 25130.08s}
│  │  ├─ asan [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 0.00s}
│  │  ├─ asv [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 97881.63s}
│  │  │  └─ limit [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 94682.16s}
│  │  ├─ bdr [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 375.66s}
│  │  ├─ compute [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 2055.17s}
│  │  │  └─ limit [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 0.00s}
│  │  ├─ ops [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 0.00s}
│  │  └─ system [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 1965.04s}
│  └─ medium [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 149389.79s}
│     ├─ adesk [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 1393.66s}
│     ├─ anet [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 7420.95s}
│     ├─ asan [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 35287.16s}
│     ├─ asv [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 40289.63s}
│     │  └─ limit [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 2217.09s}
│     ├─ bdr [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 4155.80s}
│     ├─ compute [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 60842.59s}
│     │  └─ limit [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 54688.07s}
│     ├─ ops [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 0.00s}
│     └─ system [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 0.00s}
└─ unstrict [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 36334.28s}
   ├─ adesk [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 0.00s}
   ├─ anet [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 0.00s}
   ├─ asan [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 4795.15s}
   ├─ asv [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 31532.34s}
   ├─ bdr [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 6.79s}
   ├─ compute [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 0.00s}
   ├─ ops [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 0.00s}
   └─ system [share]  {aff_low_pct: 70, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 0.00s}
network [share]  {aff_low_pct: -1, cpus: 0-7, shares: 1024, quota: -1, mems: 0, usage: 615927.11s}
├─ control [share]  {aff_low_pct: -1, cpus: 0-7, shares: 1024, quota: -1, mems: 0, usage: 615927.11s}
└─ forward [monopoly]  {aff_low_pct: -1, cpus: 0, shares: 1024, quota: -1, mems: 0, usage: 0.00s}
storage [share]  {aff_low_pct: -1, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 7158.89s}
├─ svc_fsd [share]  {aff_low_pct: -1, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 4407.02s}
├─ svc_mds [share]  {aff_low_pct: -1, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 0.00s}
├─ svc_nfs [share]  {aff_low_pct: -1, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 2500.72s}
├─ svc_ssdc [share]  {aff_low_pct: -1, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 0.00s}
├─ svc_tgtd [share]  {aff_low_pct: -1, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 251.14s}
├─ svc_tierd [share]  {aff_low_pct: -1, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 0.00s}
└─ svc_vhost [share]  {aff_low_pct: -1, cpus: 4-7, shares: 1024, quota: -1, mems: 0, usage: 0.00s}
sys-fs-fuse-connections.mount  {aff_low_pct: -1, shares: 1024, usage: 0.00s, quota: -1}
sys-kernel-debug.mount  {aff_low_pct: -1, shares: 1024, usage: 0.00s, quota: -1}
sys-kernel-tracing.mount  {aff_low_pct: -1, shares: 1024, usage: 0.00s, quota: -1}
system.slice  {aff_low_pct: -1, shares: 1024, usage: 2877.68s, quota: -1}
│    # Dismissed subgroups (28 subgroups)
user.slice  {aff_low_pct: -1, shares: 1024, usage: 0.00s, quota: -1}
```