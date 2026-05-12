---
sidebar_position: 1
---

# start

### Overview

Start the vtpperlproxy service

### Command Parameters

No parameters

### Usage Example

```bash
acli service asv vtpperlproxy start
```

### Output Example
```bash
acli service asv vtpperlproxy start

 Physical cores < 16: 8checking before start: getcmdpid return 0, get pids: 4135746 4135749:checking before start: getcmdpid2 return 1, get pids: :Start (supervisor --flag-file '/var/run/vtpperlproxy.pid' --flag 010 -p '/sf/bin/vtpperlproxy,*vtpperlproxy' '/sf/bin/vtpperlproxy') OK!.
```