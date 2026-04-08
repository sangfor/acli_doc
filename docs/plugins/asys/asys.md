---
sidebar_position: 1
---

# asys

### 操作概述

执行系统检查工具对主机进行检测

### 命令参数

```bash
-s=string                （必要参数），子命令选择，枚举值：
                              - offline（检查系统离线状态）
                              - all（运行所有检查）
                              特殊格式：<command>:help 显示特定命令的详细帮助，示例：offline:dmesg
                                    - dmesg（检查 dmesg 日志）
                                    - ipmi（检查 IPMI 日志）
                                    - w3（检查三无场景日志）
-b=string                开始时间，格式：YYYY-MM-DD HH:MM:SS，示例：2025-10-27 02:30
-e=string                结束时间，格式：YYYY-MM-DD HH:MM:SS，示例：2025-10-27 12:30
-t=string                日期，格式：YYYY-MM-DD，示例：2025-10-27（与 -b/-e 互斥，使用 -t 则时间自动补全为全天）
-d=string                仅调试模式（-D）下可用，指定目录，示例：/tmp。
                              根据-s中的不同特殊格式有不同的行为：
                                    - 对于dmesg，自动发现dmesg后缀文件，根据时间确定要分析的dmesg
                                    - 对于ipmi，默认分析ipmi的日志文件 ipmi.log
                                    - 对于w3，对目录下的所有日志做关键字分析和时间戳分析
-D|--debug               启用调试模式
-c|--cmd_info            以 JSON 格式显示命令信息
-h|--help                显示帮助信息
-v|--version             显示版本信息
```

### 使用示例

```bash
# 示例1：显示命令帮助
asys -s offline:help

# 示例2：检查系统离线状态（指定时间范围）
asys -s offline -b "2025-10-27 02:30" -e "2025-10-27 12:30"

# 示例3：检查系统离线状态（指定日期，自动覆盖全天）
asys -s offline -t "2025-10-27"

# 示例4：检查 dmesg 日志（指定时间范围）
asys -s offline:dmesg -b "2025-10-27 02" -e "2025-10-27 10"

# 示例5：检查 dmesg 日志（指定日期）
asys -s offline:dmesg -t "2025-10-27"

# 示例6：检查 IPMI 日志（指定时间范围）
asys -s offline:ipmi -b "2025-10-27 06:30" -e "2025-10-27 18:30"

# 示例7：检查 IPMI 日志（指定日期）
asys -s offline:ipmi -t "2025-10-27"

# 示例8：检查 w3 日志（指定时间范围）
asys -s offline:w3 -b "2025-10-27 09" -e "2025-10-27 11"

# 示例9：检查 w3 日志（指定日期）
asys -s offline:w3 -t "2025-10-27"

# 示例10：运行所有检查
asys -s all -t "2025-10-27"
```

### 结果示例

```bash
------------------------------------------------------
[asys] 工具开始运行...
时间范围不能超过30天
[asys] User params: s=offline:dmesg, b=2025-10-27 02, e=2025-10-27 10, t=, d=, D=false------------------------------------------------------
工具版本：1.1.60, 发布日期：2026-03-04
工具执行命令：/sf/data/local/acli/plugins/asys/plugin -s offline:dmesg -b 2025-10-27 02 -e 2025-10-27 10
当前日期：2026-04-08
如果需要上升技术支持，请收集日志并上传到日志服务器，参考命令如下：
acli log_collect create -s [工单号] -m offline -d [问题日期，如YYYY-MM-DD]
[asys] 可收集插件Asys的日志进一步分析: /sf/log/today/acli/plugin/acli_plugins_asys.log
------------------------------------------------------
```
