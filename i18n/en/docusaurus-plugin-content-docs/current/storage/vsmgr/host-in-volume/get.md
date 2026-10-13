---
sidebar_position: 1
---

# get

### Overview

Query whether a host is in a VS volume

### Command Parameters

```bash
-h|--hosts=string   Required parameter, Host names, multiple separated by commas, example: host-0050568ec35e or host-a,host-b
```

### Usage Example

```bash
acli storage vsmgr host-in-volume get --hosts host-0050568ec35e
```

### Output Example

1 = in the volume with data/hot-spare disks, 0 = not in the volume or none.

```bash
{"host-0050568ec35e": 1}
```
