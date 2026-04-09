---
sidebar_position: 1
---

# collect_log

### 操作概述

以虚拟机为单位，自动监控虚拟机，自动检测虚拟机和所在主机，并将相关日志进行打包

### 命令参数

```bash
-d|--date=string              需要收集的时间，默认现在，格式：2006-01-02 15:04:05
--duration=integer            收集日志对虚拟机监控时间，单位分钟，默认5分钟（默认：5）
--no-monitor                  收集日志不对虚拟机进行监控，默认进行监控
-v|--vmid=string              （必要参数）需要收集的虚拟机，示例：6025407369236
```

### 使用示例

```bash
# 示例1：收集指定虚拟机的日志（使用默认监控时间）
acli performance_tools combined collect_log -v 6025407369236

# 示例2：收集指定虚拟机的日志（指定监控时间）
acli performance_tools combined collect_log -v 6025407369236 --duration 10

# 示例3：收集指定时间和虚拟机的日志
acli performance_tools combined collect_log -v 6025407369236 -d "2025-06-25 10:30:00"

# 示例4：收集虚拟机的日志但不进行监控
acli performance_tools combined collect_log -v 6025407369236 --no-monitor
```

### 结果示例

```bash
开始监控虚拟机6025407369236，时间1分钟
开始检查虚拟机6025407369236...
开始检查主机...
开始收集日志...
开始收集配置文件...
开始收集日志文件...
开始收集命令输出...
开始收集告警信息...
开始收集操作日志...
开始压缩文件夹: /sf/data/local/performance_tools/collect_log_v2_20260408_20260408
打包成功, 文件名: /sf/data/local/performance_tools/collect_log_v2_20260408_20260408.zip
```
