---
sidebar_position: 10
---

# check
操作概述: 查看目标主机的端口是否畅通

命令参数:
```bash
-H|--host=string 主机名
-p|--port=integer 端口号
```

使用示例:
```bash
acli network port check -H localhost -p 10000
```

结果示例:
```bash
成功连接到目标端口
====or====
错误：执行失败：连接到目标端口超时
```