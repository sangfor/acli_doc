---
sidebar_position: 2
---

# set

### Overview

Set the VM status

### Command Parameters

```bash
-v|--vm-id=string            Required parameter, VM ID, example: 1268314679221
-e|--error-state=string      Required parameter, error state, example: UPDATE_SUCCESS
```

### Usage Example

```bash
acli vm status set -v 1268314679221 -e UPDATE_SUCCESS
```

### Output Example

```bash
errorState: NoError
powerState: On
taskState: Idle
vmID: 1268314679221
vmStatus: Running
```
