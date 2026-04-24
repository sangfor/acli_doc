---
sidebar_position: 1
---

# set

### 操作概述

修改操作队列配置

### 命令参数

```bash
  -w|--work=integer                   进程操作队列最大工作数，示例：13
  -W|--wait=integer                   进程操作队列最大等待数，示例：1000
  -p|--pressure-work=integer          进程操作压力队列最大工作数，取值范围0-9999，示例：4
```

### 使用示例

```bash
acli service asv vtpdaemon opqueue config set -w 14 -W 999
```

### 结果示例

```bash
正常案例：
OK
```
