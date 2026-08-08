---
sidebar_position: 10
---

# get

操作概述: 获取进程操作队列配置

命令参数: 无

使用示例:

```bash
acli platform cfs vtp_process_op_queue get
```

结果示例:

```bash
{
  "process_op_queue_max_working": 13,
  "process_op_queue_max_waiting": 1000,
  "process_op_pressure_queue_max_working": 4
}
```