---
sidebar_position: 10
---
 
# get
操作概述: 获取过载保护功能相关维护信息
 
命令参数: 
```bash
-s|--status=flag                从redis中查看过载保护状态、CPULevel、隔离状态下的隔离核数
-b|--boot-process=flag          查看loadman首次启动的进程信息
-c|--cgroup-information=flag    查看cgroup信息
-p|--parameter=flag             查看loadman服务启动参数
```
 
使用示例:
```bash
acli service asv loadman maintenance get -b
```
 
结果示例:
```bash
3109603
```