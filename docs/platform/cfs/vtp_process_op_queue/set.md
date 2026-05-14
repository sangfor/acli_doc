---
sidebar_position: 10
---

# set

操作概述: 设置进程操作队列配置

命令参数:

```bash
-w|--max-working=integer 进程操作队列最大工作数，示例：13，取值范围1-9999
-n|--max-waiting=integer 进程操作队列最大等待数，示例：1000，取值范围1-9999
-p|--pressure-max-working=integer 进程操作压力队列最大工作数，示例：4，取值范围0-9999
```

使用示例:

```bash
acli platform cfs vtp_process_op_queue set --max-working 13
acli platform cfs vtp_process_op_queue set --max-working 13 --max-waiting 1000 --pressure-max-working 4
```

结果示例:

```bash
SUCCESS: process_op_queue_max_working=13
```