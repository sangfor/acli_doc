---
sidebar_position: 1
---

# get

### 操作概述

获取虚拟机状态

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机id，示例：2848367193475
```

### 使用示例

```bash
acli vm status get -v 1072335336316
```

### 结果示例

```bash
clockSkew: 0
errorState: NoError 
lastRunHostID:
operatorName: 
powerState: Off 
runningHosts: 
startedAt:
taskState: Idle 
terminatedAt: 
vmID: 2594568509217 
vmStatus: Stopped
```
