---
sidebar_position: 1
---

# verify

### Overview

Verify the integrity and consistency of the CBT file

### Command Parameters
```bash
-f|--filename=string    Required parameter, Specifies the absolute path of the disk file to verify the CBT functionality of the file, Example: /sf/xxx/vm-disk-1.qcow2
```

### Usage Example

```bash
acli platform backup cbt file verify -f="/disks/83/b1/019b69cf-c958-760c-8e49-83b13ebec9c7/vm-disk-1.qcow2"
```

### Output Example

```bash
Correct Example:
0
Error case: A non-zero output indicates an abnormal CBT state.
```