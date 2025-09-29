---
sidebar_position: 10
---

# pidstat
操作概述: 调用系统pidstat命令

命令参数:
```bash
无
```

使用示例:
```bash
acli system pidstat
```

结果示例:
```bash
Linux 4.18.0-6.10.0_R2 (host-005056893c9d)      08/27/2025      _x86_64_        (8 CPU)

02:36:08 PM   UID       PID    %usr %system  %guest   %wait    %CPU   CPU  Command
02:36:08 PM     0         1    0.00    0.01    0.00    0.00    0.01     6  init
02:36:08 PM     0         2    0.00    0.00    0.00    0.00    0.00     2  kthreadd
02:36:08 PM     0         9    0.00    0.01    0.00    0.04    0.01     0  ksoftirqd/0
02:36:08 PM     0        10    0.00    0.11    0.00    0.27    0.11     7  rcu_sched
02:36:08 PM     0        11    0.00    0.00    0.00    0.00    0.00     0  migration/0
02:36:08 PM     0        15    0.00    0.00    0.00    0.00    0.00     1  watchdog/1
02:36:08 PM     0        16    0.00    0.02    0.00    0.00    0.02     1  migration/1
02:36:08 PM     0        17    0.00    0.07    0.00    0.26    0.07     1  ksoftirqd/1
02:36:08 PM     0        21    0.00    0.00    0.00    0.00    0.00     2  watchdog/2
02:36:08 PM     0        22    0.00    0.02    0.00    0.00    0.02     2  migration/2
02:36:08 PM     0        23    0.00    0.09    0.00    0.29    0.09     2  ksoftirqd/2
02:36:08 PM     0        28    0.00    0.01    0.00    0.00    0.01     3  migration/3
02:36:08 PM     0        29    0.00    0.11    0.00    0.38    0.11     3  ksoftirqd/3
02:36:08 PM     0        34    0.00    0.02    0.00    0.00    0.02     4  migration/4
02:36:08 PM     0        35    0.00    0.09    0.00    0.29    0.09     4  ksoftirqd/4
...
```