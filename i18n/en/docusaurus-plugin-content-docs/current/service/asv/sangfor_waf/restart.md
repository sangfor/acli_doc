---
sidebar_position: 1
---

# restart

### Overview

Restart sangfor_waf service

### Command Parameters

No parameters

### Usage Example

```bash
acli service asv sangfor_waf restart
```

### Output Example
```bash
acli service asv sangfor_waf restart

Stoping sangfor_waf: :checking stop status: getcmdpid return 1, get pids: :  OK!.
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Start (supervisor --lock-file '/var/run/supervisor/sangfor_waf.suplock' --flag-file '*' --flag 011 --prerun 'bash /sf/bin/sangfor_waf_prepare.sh' -w '/sf/waf/local/nginx/sbin/sangfor_waf -e /sf/log/sangfor_waf/sangfor_waf.log -p /sf/waf/local/nginx') OK!.
```