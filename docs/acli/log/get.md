---
sidebar_position: 10
---

# get
操作概述: 查询acli工具的debug日志信息

命令参数:
```bash
-c|--context=integer      输出上下文的行数
-p|--pattern=string       正则表达式
-d|--date=string          指定日志的日期，格式YYYY-MM-DD
-a|--all=flag             展示所有登录用户的日志
-l|--level=string         展示指定级别的日志，枚举值：debug，info，warning，error，critical
```

使用示例:
```bash
# 查询debug级别的日志信息
acli acli log get -l debug
```

结果示例:
```bash
2025-03-21 10:34:22 [DEBUG] Starting acli command execution
2025-03-21 10:34:23 [INFO] Command executed successfully
2025-03-21 10:34:24 [WARNING] Potential performance issue detected
```