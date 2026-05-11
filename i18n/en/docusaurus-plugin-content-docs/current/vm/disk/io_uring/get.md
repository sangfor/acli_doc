---
sidebar_position: 1
---

# get

### Overview

Check the virtual machine io_uring status

### Command Parameters
```bash
-v|--vm-id=string           Required parameter, VM id, e,g. 1234567890123
```

### Usage Example

```bash
acli vm disk io_uring get -v 2749923911666
```

### Output Example

```bash
# Indicated by %; for example, an output of 100% means one logical core is being occupied.
CPU Usage: 20.8%
# Entering a non-existent virtual machine ID will result in no output.
```