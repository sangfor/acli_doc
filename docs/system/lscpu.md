---
sidebar_position: 1
---

# lscpu

### 操作概述

查看 CPU 架构信息（架构、型号、核数、线程数等，只读）。

### 命令参数

无参数

### 使用示例

```bash
acli system lscpu
```

### 结果示例

```bash
# acli system lscpu
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                32
On-line CPU(s) list:   0-31
Thread(s) per core:    2
Core(s) per socket:    16
Socket(s):             1
Model name:            Intel(R) Xeon(R) Gold 5220R CPU @ 2.20GHz
```
