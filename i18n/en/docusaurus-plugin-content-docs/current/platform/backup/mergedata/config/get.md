---
sidebar_position: 1
---

# get

### Overview

Get the content of the data merge task configuration file merge_data.json

### Command Parameters
```bash
No parameters
```

### Usage Example

```bash
acli platform backup merge_data config get
```

### Output Example

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