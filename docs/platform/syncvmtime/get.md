---
sidebar_position: 1
---

# get

### 操作概述

查询集群虚拟机时间同步配置

### 命令参数

```bash
无参数
```

### 使用示例

```bash
acli platform syncvmtime get
```

### 结果示例

```bash
{
  "startup_sync_enable": 1,
  "timing_sync_enable": 0,
  "timing_sync_hw_clock": 1,
  "timing_sync_smooth": 0,
  "timing_sync_time_interval": 64,
  "timing_sync_tinker_panic": 0
}
```
