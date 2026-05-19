---
sidebar_position: 1
---

# get

### 操作概述

查询调度器配额

### 命令参数

无参数

### 使用示例

```bash
acli platform scheduler quota get
```

### 结果示例

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
