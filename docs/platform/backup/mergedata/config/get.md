---
sidebar_position: 1
---

# get

### 操作概述

查询数据整理任务配置文件merge_data.json的内容

### 命令参数

```bash
无
```

### 使用示例

```bash
acli platform backup merge_data config get
```

### 结果示例

```bash
{
  "cancel_interval": 1802,
  "merge_task_info": {},
  "running_interval": 61,
  "task_cancel_time": {
    "5335754095258": {
      "last_cancel_time": "1770280793"
    },
    "5645952907764": {
      "last_cancel_time": "1773058995"
    },
    "2822858671240": {
      "last_cancel_time": "1770280794"
    },
    "460679425634": {
      "last_cancel_time": "1770101205"
    }
  },
  "volume_recovery_task_info": {},
  "block_stream_status": {},
  "stopped_interval": 301
}

```
