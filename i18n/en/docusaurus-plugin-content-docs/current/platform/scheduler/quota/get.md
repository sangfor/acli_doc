---
sidebar_position: 1
---

# get

### Overview

Query scheduler quota

### Command Parameters

No parameters

### Usage Example

```bash
acli platform scheduler quota get
```

### Output Example

```bash
activeTask:
  ClusterQuota: 5000
  FaultToleranceQuota: 0
  NodeQuota: 0
  ResourceType: activeTask
computeOperate:
  ClusterQuota: 600
  FaultToleranceQuota: 0
  NodeQuota: 25
  ResourceType: computeOperate
storageWrite:
  FaultToleranceQuota: 0
  NodeQuota: 2
  ResourceType: storageWrite
volumeOperateAgent:
  ClusterQuota: 256
  FaultToleranceQuota: 0
  NodeQuota: 10
  ResourceType: volumeOperateAgent
volumeOperateServer:
  ClusterQuota: 256
  FaultToleranceQuota: 0
  NodeQuota: 256
  ResourceType: volumeOperateServer
```