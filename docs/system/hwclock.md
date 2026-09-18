---
sidebar_position: 1
---

# hwclock

### 操作概述

查询硬件时钟时间

### 命令参数

```bash
-r|--show=flag      显示 RTC 时间（默认行为）
-v|--verbose=flag   详细输出
--get=flag          显示 drift 校正后的 RTC 时间
-V|--version=flag   显示版本信息
```

### 使用示例

```bash
acli system hwclock -r
```

### 结果示例

```bash
2026-09-09 10:07:03.992012+08:00
```
