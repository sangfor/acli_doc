---
sidebar_position: 2
---

# set

### Overview

Set CPU consistency, modify DB and CFS config based on the specified sockets and cores per socket (Dangerous operation: will overwrite existing configuration)

### Command Parameters

```bash
-v|--vm-id=string                 Required parameter, VM ID. Example: 614182240912
-s|--sockets=integer              Optional parameter, force specify CPU sockets. Example: 2
-c|--cores-per-socket=integer     Optional parameter, force specify cores per socket. Example: 1
```

### Usage Example

```bash
# Set both sockets and cores per socket
acli vm cpu consistency set -v 614182240912 -s 2 -c 1

# Set sockets only
acli vm cpu consistency set -v 614182240912 -s 1
```

### Output Example

```bash
Are you sure you want to execute the operation? (y[es]/n[o]): y
{"VMID":"614182240912","SocketsBefore":1,"SocketsAfter":2,"CoresPerSocketBefore":1,"CoresPerSocketAfter":1}
```