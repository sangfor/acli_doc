---
sidebar_position: 1
---

# iperf3

### 操作概述

网络带宽测量诊断工具，测量 TCP/UDP 吞吐量（只读，不改系统状态）。命令在 vs-cp-manager 容器内执行（与 vs 容器共享网络命名空间）。

### 命令参数

本命令为部分只读命令，选项不设白名单（默认放通），但下列黑名单参数命中即拒绝。

禁止参数清单（命中即拒绝，含 GNU 唯一前缀缩写）：

```bash
--logfile=<file>  将日志写入文件，属写操作，拒绝执行；
                  因 GNU getopt 支持唯一前缀缩写，--lo 开头的写法（--lo / --log）同样命中拒绝；
                  注意 --length 不受影响（其最短唯一前缀为 --le）
```

### 使用示例

```bash
acli system iperf3 -c 127.0.0.1 -p 5201 -t 5
```

### 结果示例

```bash
# acli system iperf3 -c 127.0.0.1 -p 5201 -t 5
Connecting to host 127.0.0.1, port 5201
[  4] local 127.0.0.1 port 51234 connected to 127.0.0.1 port 5201
[ ID] Interval           Transfer     Bitrate
[  4]   0.00-5.00  sec   1.10 GBytes  1.89 Gbits/sec                  sender
[  4]   0.00-5.00  sec   1.10 GBytes  1.89 Gbits/sec                  receiver

iperf Done.
```