---
sidebar_position: 1
---

# get

### Overview

View the number of interface queues

### Command Parameters
```bash
-n|--nic-name=string    Required parameter, Interface name, Example: eth1, channel1
```

### Usage Example

```bash
acli network nic queue get --nic-name eth4
```

### Output Example

```bash
eth4
   ring_count:
      current: 0
      max: 0
      initial: 0
   name: eth4
   id: eth4
```