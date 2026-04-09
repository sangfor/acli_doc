---
sidebar_position: 1
---

# start

### 操作概述

监控（磁盘 IO、VS IO、虚拟机 IO、pidstat、网络）信息存储文件中

### 命令参数

```bash
-c|--core=string              监控项，监控 CPU 信息；示例：'1,2,3'，全部核心'all'
-s|--disk=string              监控项，监控磁盘设备；示例：'sda,sdb'，全部磁盘'all'
-d|--duration=interger        监控时间，单位天（默认：1）
-f|--frequency=interger       监控频率，单位秒（默认：2）
-n|--net=string               监控项，监控网卡信息；示例：'eth1,eth2'，全部网卡'all'
-p|--pid=string               监控项，监控进程信息；示例：'pid1,pid2'，全部进程'all'
-v|--vm=string                监控项，监控 VM 信息；指定虚拟机 vmid，目前仅支持一个 vmid
-i|--vs=bool                  监控项，监控虚拟存储
--lang=string                 设置命令行输出语言，可选项：zh_CN、en_US（全局参数）
-h|--help                     显示帮助信息
```

### 使用示例

```bash
# 示例1：监控指定磁盘设备
acli performance_tools monitor start -s sda,sdb

# 示例2：监控全部磁盘设备
acli performance_tools monitor start -s all
```

### 结果示例

```bash
程序启动，pid： 1337319
```
