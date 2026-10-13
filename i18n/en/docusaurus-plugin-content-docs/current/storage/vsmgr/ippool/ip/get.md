---
sidebar_position: 1
---

# get

### Overview

Query IPs allocated to a host in a specified-type IP pool

### Command Parameters

```bash
-t|--type=string   Required parameter, IP usage type, currently only supports OverVolume (volume oversubscription VIP pool), example: OverVolume. enum=['OverVolume']
-H|--host=string   Required parameter, Host name, example: host-0050568ec35e
```

### Usage Example

```bash
acli storage vsmgr ippool ip get --type <string> --host host-0050568ec35e
```

### Output Example

No output when unallocated or the IP pool is not configured; an error message is also output when the IP pool is not configured.

```bash
192.168.1.100
```
