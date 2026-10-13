---
sidebar_position: 5
---

# delete

### Overview

Delete a Priority Flow Control (PFC) configuration (asynchronous task, returns taskId)

### Command Parameters

```bash
-f|--flowcontrol-id=string    Required parameter, Flow control configuration ID (UUID), e.g. 6728081d-cb8b-4be1-ba35-28158e150dd4
```

### Usage Example

```bash
# First list to get the id
acli network pfc list -d 960d7a90-aad3-4f5c-b57f-5e3f61098ae2

# Delete
acli network pfc delete -f 215613f8-4ee3-4d56-a602-d05fe9cd484c
```

### Output Example

```bash
taskId: host-0050568ecad9:1703505480:2
```
