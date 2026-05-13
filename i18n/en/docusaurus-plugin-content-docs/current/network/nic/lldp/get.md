---
sidebar_position: 1
---

# get

### Overview

View interface LLDP

### Command Parameters
```bash
-n|--nic-name=string    Required parameter, Port name, example: eth1
```

### Usage Example

```bash
acli network nic lldp get --nic-name eth2
```

### Output Example

```bash
hasMultiNeighbors: 0
ifaceName: eth2
local:
    aggregationNum: 0
    maxFrameSize: 1518
    vlanId: 0
mode: RXTX
enabled: 1
```