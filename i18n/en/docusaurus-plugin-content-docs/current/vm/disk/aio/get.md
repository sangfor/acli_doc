---
sidebar_position: 1
---

# get

### Overview

Check the AIO info of the specified disk of virtual machine

### Command Parameters
```bash
-v|--vm-id=string           Required parameter, VM id, e,g. 1234567890123
-d|--disk=string            Required parameter, VM disk name, e,g. vm-disk-1.qcow2
```

### Usage Example

```bash
acli vm disk aio get -v 2749923911666 -d vm-disk-1.qcow2
```

### Output Example

```bash
# Virtual machines use io_uring mode
io_uring
# Virtual machines use Linux-AIO mode
native
# If a non-existent VM ID or an incorrect disk name is provided, no output will be generated.
```