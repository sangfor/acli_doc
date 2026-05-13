---
sidebar_position: 1
---

# restart

### Overview

Restart the pmxcfs service

### Command Parameters

No parameters

### Usage Example

```bash
acli service asv pmxcfs restart
```

### Output Example
```bash
acli service asv pmxcfs restart

Stoping pmxcfs: :checking stop status: getcmdpid return 0, get pids: 52468: .checking stop status: getcmdpid return 0, get pids: 52468: .checking stop status: getcmdpid return 0, get pids: 52468: .checking stop status: getcmdpid return 1, get pids: :  OK!.
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Start (/sf/cluster/bin/pmxcfs -f -w &) OK! 4124167.
```