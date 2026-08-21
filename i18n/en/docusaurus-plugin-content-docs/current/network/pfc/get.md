---
sidebar_position: 2
---

# get

### Overview

Query a single Priority Flow Control (PFC) configuration (filtered by domainId, returns the first match; backend has no get-by-id endpoint)

### Command Parameters

```bash
-d|--domain-id=string    Required parameter, network plane ID (UUID) used to filter flow control configurations
```

### Usage Example

```bash
acli network pfc get -d 960d7a90-aad3-4f5c-b57f-5e3f61098ae2
```

### Output Example

```bash
[0]:
  cnpDscp: 48
  cnpPrio: 3
  domainId:
    [0]: 960d7a90-aad3-4f5c-b57f-5e3f61098ae2
  dscpTag: 26
  enable: true
  id: 215613f8-4ee3-4d56-a602-d05fe9cd484c
  trust: dscp
```
