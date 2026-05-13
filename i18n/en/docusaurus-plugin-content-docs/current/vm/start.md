---
sidebar_position: 1
---

# start

### Overview

Power on VM

### Command Parameters
```bash
-v|--vm-id=string           Required parameter, VM ID, Example: 4872898137715
```

### Usage Example

```bash
acli vm start -v 1072335336316
```

### Output Example

```bash
# Failed
HTTP Status Code: 511 - Virtual machine (1323297949124) does not exist.

# Success (Asynchronous Task)
host-0050568e723c:1797593:1775785841:3009749796815

# Query Asynchronous Task Results and Virtual Machine Status
acli task get -v 4872898137715 -l 1
acli vm status get -v 4872898137715
```