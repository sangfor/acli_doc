---
sidebar_position: 1
---

# get

### 操作概述

获取平台日志

### 命令参数

```bash
-k|--keyword=string       搜索关键字，示例：序列号
-i|--request-id=string    调用链request_id，示例：82ab4228259a3f227b763dd0cc6b53df
-t|--time=string          指定时间，格式：'YYYY-MM-DD HH:MM:SS'、'YYYY-MM-DD HH'
-f|--file=string          指定文件，不能包含路径，示例：sfvt_vtpdaemon.log
-c|--context=integer      指定上下文行数，示例：2，3
-E|--extend=flag          针对--keyword参数使用扩展的正则表达式
-p|--path=string          指定搜索的绝对路径，只能指定/sf/log目录和/sf/data/local下的文件或者目录，不指定默认搜索/sf/log目录下的内容。
仅支持路径指定的目录名或者文件名使用通配符*，路径需要使用引号包裹，示例：'/sf/log/today/' '/sf/log/today/sfvt*'
-g|--gzip=flag            针对 --path 参数，支持搜索 .gz 文件的内容。
但如果 --path 是一个目录，则仅能搜索该目录下的子文件，无法搜索更深层次的文件。

说明：
不支持跨主机检索，如需检索其他主机请ssh到对应主机
不指定时间默认检索目录是/sf/log，建议指定日期提高检索效率

示例1：指定时间，可自动解压白盒日志，快速查看本主机在6号，错误码为0x010019FA的日志
acli log get -t '2025-06-06' -k 0x010019FA

示例2：指定报错，快速查看本主机包含：‘备份报表数据失败’字段的sfvt_vtpdaemon.log日志
acli log get -k '备份报表数据失败' -f sfvt_vtpdaemon.log

示例3：指定调用链，快速查看本主机/sf/data/local下request_id为：‘82ab4228259a3f227b763dd0cc6b53df’的日志
acli log get -i 82ab4228259a3f227b763dd0cc6b53df -p /sf/data/local
```

### 使用示例

```bash
acli log get -k "info" -f sfvt_vtpsh.log
```

### 结果示例

```bash
/sf/log/21/sfvt_vtpsh.log:2025-07-21 21:39:11.366806 info [sfvt_vtpsh] 21:39:11.366 I 61678 Register.pm(VTP::xx):41 | [7v2#Gq10F3k.0.0] [register_replace] register replace(DataReport process_when_controller_change).
/sf/log/21/sfvt_vtpsh.log:2025-07-21 21:39:11.499877 info [sfvt_vtpsh] 21:39:11.499 I 61678 Register.pm(VTP::xx):32 | [7v2#Gq10F3k.0.0] [register_precheck] register precheck(DBManager check_replace).
/sf/log/21/sfvt_vtpsh.log:2025-07-21 21:39:11.499931 info [sfvt_vtpsh] 21:39:11.499 I 61678 Register.pm(VTP::xx):41 | [7v2#Gq10F3k.0.0] [register_replace] register replace(DBManager deal_replaced_db_nodes).
```
