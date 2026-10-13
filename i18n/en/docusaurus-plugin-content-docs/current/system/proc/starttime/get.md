---
sidebar_position: 1
---

# get

### Overview

Get the start time of a specified process

### Command Parameters

```bash
-p|--process-name=string   Required parameter, Process name (must be unique, otherwise the first matched process is used), example: vtsn_tool
```

### Usage Example

```bash
acli system proc starttime get --process-name vtsn_tool
```

### Output Example

Outputs a second-level epoch timestamp.

```bash
1788910717
```
