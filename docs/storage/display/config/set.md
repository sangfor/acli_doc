---
sidebar_position: 1
---

# set

### 操作概述

设置是否展示可用空间大于等于100G的Local系统盘

### 命令参数

```bash
-a|--allow-small-local-disk=integer    必要参数，是否展示可用空间大于等于100G的Local系统盘，枚举值（必填）：0（不展示），1（展示）
```

### 使用示例

```bash
acli storage display config set -a 1
```

### 结果示例

```bash
命令执行成功！
```
