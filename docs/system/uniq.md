---
sidebar_position: 1
---

# uniq

### 操作概述

过滤并输出文件或输入中相邻的重复行，支持管道输入

### 命令参数

```bash
无参数
```

该命令支持将参数原样透传给 uniq 命令，无参数限制，可配合管道使用。

### 使用示例

```bash
acli system uniq /path/to/file
```

```bash
acli system uniq -c /path/to/file
```

### 结果示例

```bash
# acli system uniq /data/app.log
line a
line b
line c
```
