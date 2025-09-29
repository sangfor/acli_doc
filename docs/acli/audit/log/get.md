---
sidebar_position: 10
---

# get
操作概述: 展示acli工具自身的审计日志

命令参数:
```bash
-c|--context=integer      输出上下文的行数
-p|--pattern=string       正则表达式
-d|--date=string          指定日志的日期，格式YYYY-MM-DD
-a|--all=flag             展示所有登录用户的日志
```

使用示例:
```bash
# 查询2025-03-21当天的审计日志
acli audit log get -d 2025-03-21
```

结果示例:
```bash
[2025-07-01 17:47:42] acli audit log get
[2025-07-01 17:47:48] acli
[2025-07-01 17:47:52] acli acli
[2025-07-01 17:48:05] acli acli audit log
[2025-07-01 17:48:09] acli acli audit log get
[2025-07-01 17:48:18] acli acli audit log get
[2025-07-01 17:48:28] acli acli audit log get
```