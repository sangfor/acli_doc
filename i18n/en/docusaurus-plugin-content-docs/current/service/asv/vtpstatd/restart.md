---
sidebar_position: 1
---

# restart

### Overview

Restart vtpstatd service

### Command Parameters

No parameters

### Usage Example

```bash
acli service asv vtpstatd restart
```

### Output Example

```bash
Stoping vtpstatd: :checking stop status: getcmdpid return 0, get pids: 24896 24914 24957 24980 24996: .checking stop status: getcmdpid return 0, get pids: 24896 24914 24957 24980 24996: .checking stop status: getcmdpid return 0, get pids: 24896 24957 24980 24996: .checking stop status: getcmdpid return 0, get pids: 24896 24957 24980 24996: .checking stop status: getcmdpid return 0, get pids: 24896 24980 24996: .checking stop status: getcmdpid return 0, get pids: 24896 24980 24996: .checking stop status: getcmdpid return 0, get pids: 24896 24980: .checking stop status: getcmdpid return 0, get pids: 24896 24980: .checking stop status: getcmdpid return 0, get pids: 24896 24980: .checking stop status: getcmdpid return 0, get pids: 24896 24980: . failed!
 -TERM time out, trying -KILL: : .  OK!.
checking before start: getcmdpid return 1, get pids: :Start (/sf/bin/vtpstatd &) OK!.
```