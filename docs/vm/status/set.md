---
sidebar_position: 2
---

# set

### 操作概述

设置虚拟机状态

### 命令参数

```bash
-v|--vm-id=string        必要参数，虚拟机id，示例：1268314679221
-e|--error-state=string  必要参数，错误状态，示例：UPDATE_SUCCESS
```

### 使用示例

```bash
acli vm status set -v 1268314679221 -e UPDATE_SUCCESS
```

### 结果示例

```bash
errorState: NoError
powerState: On
taskState: Idle
vmID: 1268314679221
vmStatus: Running
```
