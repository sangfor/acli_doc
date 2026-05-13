---
sidebar_position: 1
---

# restart

### Overview

Restart vtpdaemon service

### Command Parameters

No parameters

### Usage Example

```bash
acli service asv vtpdaemon restart
```

### Output Example
```bash
acli service asv vtpdaemon restart

Stoping vtpdaemon: :checking stop status: getcmdpid return 1, get pids: :  OK!.
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Start (supervisor --flag-file '/var/run/vtpdaemon.pid' --flag 010 -p '/sf/bin/vtpdaemon,*vtpdaemon' '/sf/bin/vtpdaemon') OK!.
```