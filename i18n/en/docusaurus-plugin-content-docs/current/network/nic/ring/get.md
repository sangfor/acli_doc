---
sidebar_position: 1
---

# get

### Overview

View the ring buffer parameters for the current interface

### Command Parameters
```bash
-n|--nic-name=string    Required parameter, Interface name, Example: eth1, channel1
```

### Usage Example

```bash
acli network nic ring get --nic-name eth4
```

### Output Example

```bash
eth4
   ring_buffer:
      current:
         rx: 1024
         tx: 512
      max:
         rx: 4096
         tx: 4096
      initial:
         rx: 1024
         tx: 512
   name: eth4
   id: eth4
```