---
sidebar_position: 1
---

# restart

### Overview

Restart the authorize_client service

### Command Parameters

No parameters

### Usage Example

```bash
acli service asv authorize_client restart
```

### Output Example
```bash
acli service asv authorize_client restart

Already stoped: authorize_client
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Start (supervisor --lock-file '/var/run/supervisor/authorize_client.suplock' --flag-file '*' --flag 011 -w '/sf/authorize/bin/authorize_client --config /sf/etc/authorize_client/authorize_client_config.json') OK!.
```