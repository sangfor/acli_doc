---
sidebar_position: 6
---

# analyze

### 操作概述

分析日志数据，找出系统、虚拟机大致瓶颈

### 命令参数

```bash
-d|--dir=string              日志文件所在目录（默认：/sf/data/local/performance_tools/performance_data）
-s|--start=string            分析日志的开始时间，未指定则检查最近1小时，格式：2006-01-02 15:04:05
-e|--end=string              分析日志的结束时间，未指定则检查最近1小时，格式：2006-01-02 15:04:05
--lang=string                设置命令行输出语言，可选项：zh_CN、en_US（全局参数）
-h|--help                   显示帮助信息
```

### 使用示例

```bash
# 示例1：分析默认目录最近1小时的日志数据
acli performance_tools analyze

# 示例2：分析指定时间范围的日志
acli performance_tools analyze -s "2025-06-25 10:00:00" -e "2025-06-25 12:00:00"

# 示例3：分析指定开始时间的日志
acli performance_tools analyze -s "2025-06-25 10:00:00"

# 示例4：分析指定目录的日志
acli performance_tools analyze -d /tmp/performance_data

# 示例5：组合使用指定目录和时间范围
acli performance_tools analyze -d /tmp/performance_data -s "2025-06-25 10:00:00" -e "2025-06-25 12:00:00"

# 示例6：显示帮助信息
acli performance_tools analyze --help
```

### 结果示例

```bash
分析日志数据，找出系统，虚拟机大致瓶颈

Usage:
  performance_tools analyze [flags]

Flags:
  -d, --dir string     日志文件所在目录 (default "/sf/data/local/performance_tools/performance_data")
  -e, --end string     分析日志的结束时间，未指定检查最近1小时，格式：2006-01-02 15:04:05
  -h, --help           help for analyze
  -s, --start string   分析日志的开始时间，未指定检查最近1小时，格式：2006-01-02 15:04:05

Global Flags:
      --lang string   设置命令行输出语言，可选项zh_CN、en_US
```
