---
sidebar_position: 1
---

# check

### Overview

Check network port status

### Command Parameters
```bash
-H|--host=string     Required parameter, Target host addr, example: 127,0.0.1
-p|--port=integer    Required parameter, Target port, example: 10000
```

### Usage Example

```bash
acli network port check -H localhost -p 10000
```

### Output Example

```bash
Successfully connected to target port
====or====
Error: Execution failed: Connection to target port timeout
```