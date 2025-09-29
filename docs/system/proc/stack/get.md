---
sidebar_position: 10
---

# get
操作概述: 查看对应pid的栈信息

命令参数:
```bash
-p|--pid=integer    查看pid对应的栈信息，示例：105667
```

使用示例:
```bash
acli system proc stack get -p 105667
```

结果示例:
```bash
[<0>] hrtimer_nanosleep+0xbe/0x1c0
[<0>] __x64_sys_nanosleep+0x6d/0x80
[<0>] do_syscall_64+0x5b/0x1d0
[<0>] entry_SYSCALL_64_after_hwframe+0x65/0xca
```