---
sidebar_position: 10
---

# top
操作概述: 调用系统top命令

命令参数:
```bash
无
```

使用示例:
```bash
acli system top
```

结果示例:
```bash
top - 22:04:32 up 14:37,  1 user,  load average: 3.18, 4.31, 4.80
Tasks: 874 total,   1 running, 758 sleeping,   0 stopped,   0 zombie
%Cpu(s): 14.6 us,  7.5 sy,  0.0 ni, 75.4 id,  0.0 wa,  1.2 hi,  1.3 si,  0.0 st
KiB Mem:  40679596 total, 28958228 used, 11721368 free,  1056720 buffers
KiB Swap: 33554428 total,        0 used, 33554428 free,  6044500 cached

   PID USER      PR  NI  VIRT  RES  SHR S  %CPU %MEM    TIME+  COMMAND
 39463 root      10 -10 65.8g 1.3g 801m S  49.3  3.4 457:05.60 dataplane
  7636 root      20   0 1276m  28m  13m S   6.6  0.1  17:17.49 containerd-squa
 80884 root      20   0 4336m 3.6g  10m S   3.6  9.4   4:21.42 perf
 55406 root      20   0 4275m 3.6g  10m S   3.3  9.3   4:25.71 perf
 49235 root      20   0     0    0    0 S   3.0  0.0  25:36.78 vhost-39067
 39881 root      20   0     0    0    0 S   2.6  0.0  20:44.26 vhost-39067
 81990 root      20   0 1739m  27m  17m S   2.6  0.1   8:45.55 mysql-managerd
121339 root      20   0 1371m 116m  45m S   2.6  0.3  16:57.39 temporal-server
 53821 root       0 -20 1721m  37m  29m S   2.3  0.1  69:44.49 pmxcfs
  7708 root      20   0 1613m 101m  41m S   2.0  0.3  31:40.71 containerd
```