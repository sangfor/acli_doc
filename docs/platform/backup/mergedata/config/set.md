---
sidebar_position: 1
---

# set

### 操作概述

修改数据整理任务配置文件merge_data.json的内容

### 命令参数

```bash
-r|--running-interval=integer       开机数据整理任务最早触发间隔，单位为秒，示例：60
-s|--stopped-interval=integer       关机数据整理任务最早触发间隔，单位为秒，示例：60
-c|--cancel-interval=integer        取消数据整理任务后的最早触发间隔，单位为秒，示例：60
```

### 使用示例

```bash
acli platform backup datamover config set -r 60 --stopped-interval 1800
```

### 结果示例

```bash
ok
```
