---
sidebar_position: 1
---

# restart

### Overview

Restart the vtplogd service

### Command Parameters

No parameters

### Usage Example

```bash
acli service asv vtplogd restart
```

### Output Example
```bash
acli service asv vtplogd restart

Stoping vtplogd: :checking stop status: getcmdpid return 0, get pids: 223957 223969 4134515: .checking stop status: getcmdpid return 0, get pids: 223957 223969 4134515: .checking stop status: getcmdpid return 0, get pids: 223957 223969 4134515: .checking stop status: getcmdpid return 0, get pids: 223957: .checking stop status: getcmdpid return 0, get pids: 223957: .checking stop status: getcmdpid return 1, get pids: :  OK!.
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Start (/sf/bin/vtplogd &) OK!.
```