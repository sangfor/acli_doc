---
sidebar_position: 1
---

# repair

### Overview

Fix shared disk expansion abnormality

### Command Parameters
```bash
-n|--name=string            Required parameter, Specify the name of the shared disk, Example: my-shared-disk

```

### Usage Example

```bash
acli vm shareddisk repair --name my-shared-disk
acli vm shareddisk repair -n my-shared-disk
```

### Output Example

```bash
Start recover shared disk, diskID=, diskName=111
Found disk: id=019d950e-efc4-7c80-bce5-369417427f43, name=111, storageId=1SANGFOR_ASAN-03d-8c51-4bbb-b896-281d5a83382a, path=/disks/36/94/019d950e-efc4-7c80-bce5-369417427f43/019d950e-efc4-7c80-bce5-369417427f43.raw
Disk is normal, no need to repair: /sf/data/1SANGFOR_ASAN-03d-8c51-4bbb-b896-281d5a83382a/disks/36/94/019d950e-efc4-7c80-bce5-369417427f43/019d950e-efc4-7c80-bce5-369417427f43.raw
Success to recover extending shared disk: 019d950e-efc4-7c80-bce5-369417427f43
```