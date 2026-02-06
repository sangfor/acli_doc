---
sidebar_position: 1
---

# check

### 操作概述

确认目标主机的对应端口是否连通

### 命令参数

```bash
-H|--host=string     必要参数，目标主机的地址，示例：127.0.0.1
-p|--port=integer    必要参数，目标主机的端口号，示例：10000
```

### 使用示例

```bash
acli network port check -H localhost -p 10000
```

### 结果示例

```bash
成功连接到目标端口
====or====
错误：执行失败：连接到目标端口超时
```
