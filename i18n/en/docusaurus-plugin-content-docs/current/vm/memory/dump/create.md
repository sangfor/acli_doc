---
sidebar_position: 1
---

# create

### Overview

Create a guest memory dump task

### Command Parameters
```bash
-v|--vm-id=string           Required parameter, VM ID, Example: 4872898137715
-p|--path=string            Required parameter, Storage directory for guest memory dumps, Note: the remaining storage space must be more than twice the guest memory size.
It is recommended to use a virtual storage path. Example: /sf/data/e8b0e860_vs_vol_rep2. Dumping 20 GB VM memory takes about 15 minutes.
```

### Usage Example

```bash
acli vm memory dump create -v 1055878891514 -p /sf/data/local
```

### Output Example

```bash
acli vm memory dump create -v 1055878891514 -p /sf/data/local
Are you sure you want to perform this operation? (y[es]/n[o]): y
Successfully dumped virtual machine memory!
```