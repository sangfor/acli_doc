---
sidebar_position: 10
---

# iostat
操作概述: 调用系统iostat命令

命令参数:
```bash
无
```

使用示例:
```bash
acli system iostat
```

结果示例:
```bash
Linux 4.18.0-6.11.1 (host-005056893b01)         08/04/2025      _x86_64_        (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          24.02    0.00   18.65    0.24    0.00   57.09

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sdb               0.12         0.52         0.07       8296       1168
sda              31.85       521.80       395.73    8246905    6254356
sdc               0.71        15.05         1.74     237914      27504
sdd               0.55        13.60         1.16     214910      18412
loop0             0.02         0.06         0.00        980         50
loop1             0.98         0.30         3.65       4778      57675
loop2             0.00         0.00         0.00         12          0
loop3             0.00         0.00         0.00          9          0
loop4             0.00         0.00         0.00         10          0
loop5             0.00         0.04         0.00        660          0
```