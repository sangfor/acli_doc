---
sidebar_position: 1
---

# list

### Overview

View the traffic mirroring policy list

### Command Parameters
```bash
-s|--start=integer    The first entry on the list, It is commonly used with a --limit parameter. Example: --start 0 --limit 10, which indicates that 10 entries will be returned, starting from entry 0., Default: 0
-l|--limit=integer    Specify the number of records to display, such as 1 or 2, Default value: 50, Default: 50
```

### Usage Example

```bash
acli network anet mirror list --start 0 --limit 1
```

### Output Example

```bash
total: 1
flow_mirrors:
    direction: All
    enable: 0
    description:
    samplingRate: 100
    dstVlan: null
    dstIfaceId: 4d3a0d8c-2f05-4592-adc8-8a9eb5efd897
    tenantId: 707e9d9dac814227b90941362efb6616
    srcIfaceIds: 8ac58d3b-5f79-40d6-af36-a5fc03d90d21
    id: c8e0562c-663d-41d6-be8c-4e6bb2617ae5
    name: qcl
```