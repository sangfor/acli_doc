---
sidebar_position: 10
---

# get
操作概述: 查看内存使用情况

命令参数:
```bash
无
```

使用示例:
```bash
acli system memory usage get
```

结果示例:
```bash
Private  +   Shared  =  RAM used        Program                                 Memcg

 64.0 KiB +  56.5 KiB = 120.5 KiB       dash                                    memory:/monopoly/noncore_group/monopoly/network_compute_group
176.0 KiB +   4.5 KiB = 180.5 KiB       vm_ipless                               memory:/monopoly/noncore_group/monopoly/network_compute_group
188.0 KiB +   5.5 KiB = 193.5 KiB       net-server                              memory:/monopoly/noncore_group
192.0 KiB +   5.5 KiB = 197.5 KiB       nc.traditional                          memory:/monopoly/noncore_group
124.0 KiB +  98.5 KiB = 222.5 KiB       net_ping_statis                         memory:/monopoly/noncore_group/monopoly/network_compute_group
208.0 KiB +  17.5 KiB = 225.5 KiB       mysqld_safe                             memory:/monopoly/noncore_group
224.0 KiB +   4.5 KiB = 228.5 KiB       acpid                                   memory:/monopoly/noncore_group
116.0 KiB + 112.5 KiB = 228.5 KiB       ce-status-monit                         memory:/monopoly/noncore_group
......
```