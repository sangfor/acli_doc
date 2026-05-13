---
sidebar_position: 1
---

# get

### Overview

View node information

### Command Parameters
```bash
-n|--node-name=string    Required parameter, Node name, generally defaults to host IP
```

### Usage Example

```bash
acli platform node get --node-name 10.131.201.84
```

### Output Example

```bash
10.131.201.84
   ip: 10.131.201.84
   id: host-005056b2a994
   master: 0
   status: 1
   alert: 0
   controller: 1
   controller_pool: 1
   name: 10.131.201.84
```