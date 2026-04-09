---
sidebar_position: 5
---

# collect_log

### 操作概述

收集主机性能相关日志、配置、命令运行结果

### 命令参数

```bash
-s|--start=string             收集日志的开始日期，默认当天，格式：2006-01-02
-e|--end=string               收集日志的结束日期，默认与开始日期一致，格式：2006-01-02
-o|--output=string            查询到的日志存放文件夹，默认存放位置为：/sf/data/local/performance_tools
-t|--type=string              指定收集的数据类型，可选值：
                                - config（配置文件）
                                - log（日志文件）
                                - command（命令输出）
                                - alert（告警信息）
                                - oplog（操作日志）
                              多个类型使用逗号分割，默认全部收集
-v|--vmids=string             指定特定的虚拟机，多个虚拟机使用逗号分割，示例：6025407369236
-g|--generate-config          生成收集日志的默认配置，里面包含了所有的收集内容
--lang=string                 设置命令行输出语言，可选项：zh_CN、en_US（全局参数）
-h|--help                     显示帮助信息
```

### 使用示例

```bash
# 示例1：收集指定日期范围的日志
acli performance_tools collect_log -s 2025-06-25 -e 2025-06-27

# 示例2：收集指定日期的日志
acli performance_tools collect_log -s 2025-06-25

# 示例3：只收集配置文件
acli performance_tools collect_log -t config

# 示例4：收集多种类型日志
acli performance_tools collect_log -t config,log,command

# 示例5：指定输出目录
acli performance_tools collect_log -o /tmp/performance_logs

# 示例6：指定特定虚拟机
acli performance_tools collect_log -v 6025407369236

# 示例7：指定多个虚拟机
acli performance_tools collect_log -v 6025407369236,6025407369237

# 示例8：组合多种参数
acli performance_tools collect_log -s 2025-06-25 -e 2025-06-27 -t config,log -v 6025407369236 -o /tmp/performance_logs

# 示例9：生成默认配置
acli performance_tools collect_log -g
```

### 结果示例

```bash
开始收集配置文件...
开始压缩文件夹: /sf/data/local/performance_tools/collect_log_v2_20260408_20260408
打包成功, 文件名: /sf/data/local/performance_tools/collect_log_v2_20260408_20260408.zip
```
