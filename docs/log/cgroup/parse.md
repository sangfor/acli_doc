---
sidebar_position: 10
---

# get
操作概述: 解析cgroup黑盒日志

命令参数:
```bash
-f|--file=string      指定cgroup黑盒日志文件，默认: /sf/log/blackbox/today/LOG_cgroup.txt
-g|--group=string     需要检索的cgroup控制器及路径，格式：<cgroup控制器>:<cgroup路径>，示例：memory:/monopoly
-p|--params=string    指定要查询的参数名称，多个参数用逗号分隔，参数可以指定控制器前缀，也可以省略前缀。示例：memory.usage_in_bytes,limit_in_bytes
```

使用示例:
```bash
acli log cgroup parse -g cpuset:/management -p cpus,preferred_cpus,mems
```

结果示例:
```bash
25-12-23 16:40:00
  cpus: 4-7
  mems: 0
25-12-23 16:40:59
  cpus: 4-7
  mems: 0
25-12-23 16:42:00
  cpus: 4-7
  mems: 0
25-12-23 16:43:00
  cpus: 4-7
  mems: 0
25-12-23 16:44:00
  cpus: 4-7
  mems: 0
25-12-23 16:45:01
  cpus: 4-7
  mems: 0
25-12-23 16:46:01
  cpus: 4-7
  mems: 0
25-12-23 16:47:02
  cpus: 4-7
  mems: 0
25-12-23 16:48:02
  cpus: 4-7
  mems: 0
25-12-23 16:49:03
  cpus: 4-7
  mems: 0
25-12-23 16:50:03
  cpus: 4-7
  mems: 0
25-12-23 16:51:04
  cpus: 4-7
  mems: 0
25-12-23 16:52:04
  cpus: 4-7
  mems: 0
```