---
sidebar_position: 1
---

# nslookup

### Overview

Perform DNS queries and get resolution records of a domain or IP (read-only).

### Command Parameters

No parameters

### Usage Example

```bash
acli system nslookup example.com
```

### Output Example

```bash
# acli system nslookup example.com
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
Name:   example.com
Address: 93.184.216.34
```
