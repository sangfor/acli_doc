---
sidebar_position: 1
---

# get

### 操作概述

查询指定进程的启动时间

### 命令参数

```bash
-p|--process-name=string   必要参数，进程名称（需保证唯一性，否则取匹配到的第一个进程），示例：vtsn_tool
```

### 使用示例

```bash
acli system proc starttime get --process-name vtsn_tool
```

### 结果示例

输出为秒级 epoch 时间戳。

```bash
1788910717
```
