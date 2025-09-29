---
sidebar_position: 10
---

# get
操作概述: 从/sf/log日志中搜索指定关键字的日志

命令参数:
```bash
-k|--keyword=string       搜索关键字
-i|--request-id=string    调用链request_id，比如82ab4228259a3f227b763dd0cc6b53df
-t|--time=string          指定时间，格式：'YYYY-MM-DD HH:MM:SS'、'YYYY-MM-DD HH'
-f|--file=string          指定文件，比如sfvt_vtpdaemon.log
-c|--context=integer      指定上下文行数，比如2，3等
-E|--extend=flag          针对--keyword参数使用扩展的正则表达式
-p|--path=string          指定搜索的绝对路径，只能指定/sf/log目录下的文件或者目录
-g|--gzip=flag            针对--path参数生效，可以搜索指定路径中的.gz文件
```

使用示例:
```bash
acli log get -k "info" -f sfvt_vtpsh.log
```

结果示例:
```bash
/sf/log/21/sfvt_vtpsh.log:2025-07-21 21:39:11.366806 info [sfvt_vtpsh] 21:39:11.366 I 61678 Register.pm(VTP::xx):41 | [7v2#Gq10F3k.0.0] [register_replace] register replace(DataReport process_when_controller_change).
/sf/log/21/sfvt_vtpsh.log:2025-07-21 21:39:11.499877 info [sfvt_vtpsh] 21:39:11.499 I 61678 Register.pm(VTP::xx):32 | [7v2#Gq10F3k.0.0] [register_precheck] register precheck(DBManager check_replace).
/sf/log/21/sfvt_vtpsh.log:2025-07-21 21:39:11.499931 info [sfvt_vtpsh] 21:39:11.499 I 61678 Register.pm(VTP::xx):41 | [7v2#Gq10F3k.0.0] [register_replace] register replace(DBManager deal_replaced_db_nodes).
```