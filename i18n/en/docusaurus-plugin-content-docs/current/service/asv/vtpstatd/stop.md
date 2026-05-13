---
sidebar_position: 1
---

# stop

### Overview

Stop the vtpstatd service

### Command Parameters

No parameters

### Usage Example

```bash
acli service asv vtpstatd stop
```

### Output Example

```bash
Stoping vtpstatd: :checking stop status: getcmdpid return 0, get pids: 38798 38799 38800 38806 38807: .checking stop status: getcmdpid return 0, get pids: 38798 38799 38800 38806 38807: .checking stop status: getcmdpid return 0, get pids: 38798 38800 38806 38807: .checking stop status: getcmdpid return 0, get pids: 38798 38800 38806 38807: .checking stop status: getcmdpid return 0, get pids: 38798 38800 38806 38807: .checking stop status: getcmdpid return 0, get pids: 38798 38800 38806 38807: .checking stop status: getcmdpid return 0, get pids: 38798 38800 38806 38807: .checking stop status: getcmdpid return 0, get pids: 38798 38800 38806 38807: .checking stop status: getcmdpid return 0, get pids: 38798 38800 38806: .checking stop status: getcmdpid return 0, get pids: 38798 38800 38806: . failed!
 -TERM time out, trying -KILL: : .  OK!.
```