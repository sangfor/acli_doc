---
sidebar_position: 1
---

# get

### Overview

Display CBT information for all disks under the VM directory

### Command Parameters
```bash
-v|--vm-dir=string     Required parameter, Specifies the disk directory path, for example: /sf/data/lv_1764129830/disks/08/57/019b4ef9-f7cd-7cdf-bee1-08571ac1ddd1/
-s|--snap-id=string    Specifies the snapshot ID, optional parameter, for example: c24a3136-6b54-4a25-9a88-8351212b259d
```

### Usage Example

```bash
acli platform backup cbt file cbtinfo get --vm-dir="/sf/data/lv_1764129830/disks/08/57/019b4ef9-f7cd-7cdf-bee1-08571ac1ddd1/" -s=b09981bc-1002-48d0-95c5-efc349cf13f1
acli platform backup cbt file cbtinfo get -v="/sf/data/lv_1764129830/disks/08/57/019b4ef9-f7cd-7cdf-bee1-08571ac1ddd1/"
```

### Output Example

```bash
{
    "019b69cf-c958-760c-8e49-83b13ebec9c7.qcow2":   4294967299
}

```