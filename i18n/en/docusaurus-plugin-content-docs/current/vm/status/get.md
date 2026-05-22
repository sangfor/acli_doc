---
sidebar_position: 1
---

# get

### Overview

Get the VM status by VM ID

### Command Parameters

```bash
-v|--vm-id=string    Required parameter, VM ID, example: 2848367193475
```

### Usage Example

```bash
acli vm status get -v 1072335336316
```

### Output Example

```bash
# Output for 6.12.0
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

# Output before 6.12.0
clockSkew:
errorState:
lastRunHostID:
operatorName:
power: 0
powerState:
runningHosts:
startedAt: 19:25:12
status: 0
taskState:
terminatedAt:
vmID: 2987661685263
vmStatus:
```
