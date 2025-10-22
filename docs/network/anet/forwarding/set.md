---
sidebar_position: 10
---

# set
操作概述: 调整转发核

命令参数:
```bash
-h|--high-performance=integer       转发核是否独占，0（关闭），1（开启）
-c|--forward-cores=integer          转发核数量，例如：8
```

使用示例:
```bash
acli network anet forwarding set -c 1
```

结果示例:
```bash
forwardCores: 1
highPerformance: true
```