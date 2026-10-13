---
sidebar_position: 1
---

# sar

### 操作概述

收集并查看系统活动报告（CPU、内存、IO 等，只读）。

### 命令参数

本命令为部分只读命令，选项不设白名单（默认放通），但下列黑名单参数命中即拒绝。

禁止参数清单（命中即拒绝）：

```bash
-o <file>  将二进制数据写入文件，属于写操作，拒绝执行
```

### 使用示例

```bash
acli system sar -u 1 5
```

### 结果示例

```bash
# acli system sar -u 1 5
Linux 4.18.0-193.el8.x86_64 (hostname)    2026-09-08

10:20:01     CPU     %user     %nice   %system   %iowait    %steal     %idle
10:20:02     all      2.50      0.00      1.00      0.00      0.00     96.50
10:20:03     all      3.00      0.00      0.50      0.00      0.00     96.50
Average:     all      2.75      0.00      0.75      0.00      0.00     96.50
```
