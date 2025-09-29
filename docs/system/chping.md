---
sidebar_position: 10
---

# chping
操作概述: 调用系统chping命令

命令参数:
```bash
无
```

使用示例:
```bash
acli system chping
```

结果示例:
```bash
usage:
chping [options]

  options:

  -h                show this help text
  -c                package count, must > 0
  -s                package size, must > 0, <= 4194279, default is 64
  -i                interval time, must > 0, default is 1,000 msec
  -t                ttl, must > 0, <= 255, default is 255
  -W                timeout, must > 0, default is 5000,000 usec
  -l <loglevel>     set loglevel(0~12), bigger level get more log.
                    log will be printed on the screen when level is bigger than or equal to 12.
  destination
```