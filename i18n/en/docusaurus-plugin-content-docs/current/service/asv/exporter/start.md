---
sidebar_position: 1
---

# start

### Overview

Start the exporter service

### Command Parameters

No parameters

### Usage Example

```bash
acli service asv exporter start
```

### Output Example

```bash
checking before start: getcmdpid return 1, get pids: :Start (supervisor --lock-file '/var/run/supervisor/exporter.suplock' --flag-file '*' --flag 011 -w '/sf/bin/exporter -f /sf/etc/datareport/exporter-api.yaml') OK! 59981.
```