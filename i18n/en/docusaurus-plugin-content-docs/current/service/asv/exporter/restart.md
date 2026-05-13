---
sidebar_position: 1
---

# restart

### Overview

Restart the exporter service

### Command Parameters

No parameters

### Usage Example

```bash
acli service asv exporter restart
```

### Output Example

```bash
Stoping exporter: :checking stop status: getcmdpid return 1, get pids: :  OK!.
checking before start: getcmdpid return 1, get pids: :Start (supervisor --lock-file '/var/run/supervisor/exporter.suplock' --flag-file '*' --flag 011 -w '/sf/bin/exporter -f /sf/etc/datareport/exporter-api.yaml') OK! 61536.
```