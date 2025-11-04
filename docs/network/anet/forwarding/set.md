---
sidebar_position: 10
---

# set
操作概述: 调整转发核

命令参数:
```bash
-h|--high-performance=integer       转发核是否独占，0（关闭），1（开启）
-c|--forward-cores=integer          转发核数量，例如：8
-s|--supthcore-exclusive=integer    是否开启超线程核独占，0（关闭），1（开启）
-v|--vm-queue-batch-size=integer    虚拟机队列批处理数，枚举值：[0, 8, 16, 32, 64, 128, 256]
```

使用示例:
```bash
acli network anet forwarding set --high-performance 1 --supthcore-exclusive 1 --vm-queue-batch-size 16
```

结果示例:
```bash
forwardCores: 1
highPerformance: true
supthcoreExclusive: true
vmQueueBatchSize: 16
```