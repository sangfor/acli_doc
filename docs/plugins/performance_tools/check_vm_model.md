---
sidebar_position: 3
---

# check_vm_model

### 操作概述

检测虚拟机业务模型

### 命令参数

```bash
-v|--vmid=string               （必要参数）指定检测的虚拟机 ID，示例：6025407369236
-d|--monitorDataDir=string      监控数据目录，添加此选项表示从监控文件中分析，否则表示实时分析，示例：/tmp/
--lang=string                   设置命令行输出语言，可选项：zh_CN、en_US（全局参数）
-h|--help                       显示帮助信息
```

### 使用示例

```bash
# 示例1：检测指定虚拟机模板（实时分析）
acli performance_tools check_vm_model -v 1649206016202

# 示例2：检测指定虚拟机模板（从监控文件分析）
acli performance_tools check_vm_model -v 1649206016202 -d /sf/data/local/monitor
```

### 结果示例

```bash
开始获取虚拟机实时数据...
开始分析虚拟机数据...
获取内存负载等级失败，内存信息为空
虚拟机磁盘平均写入速度为: 0.00 MB/s, 读取速度为: 0.00 MB/s, 写延迟：0.00 ms, 读延迟：0.22 ms, 写入块大小：0.00, 读取块大小：0.20, 写入队列深度：0, 读取队列深度：0.
虚拟机网卡平均发送速率: 0.00 MB/s, 接收速率: 0.00 MB/s
虚拟机CPU平均使用率为: usr 0.65%, sys 0.47%, wait 0.05%, guest 0.35%, util 1.48%
当前虚拟机模型为: 低负载型
分析建议：无
```
