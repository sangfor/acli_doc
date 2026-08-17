---
sidebar_position: 1
---

# convert

### Overview

Convert ordinary VMs to placeholder VMs. Convert ordinary VMs in the replica datastore to placeholder VMs. The datastores for placeholder VMs are specified by users. The vmman convert-to-placeholder API is called to issue a conversion command.

### Command Parameters

```bash
-v|--vm-id=string                     Required parameter, Source VM ID. Example: 6882173957870
-p|--placeholder-datastore-id=string  Required parameter, Datastore ID of placeholder VM. Example: 1SANGFOR_ASAN-003-5171-4ac2-b777-62d94ef8fb7b
```

### Usage Example

```bash
acli vm dr placeholder convert -v 6882173957870 -p 1SANGFOR_ASAN-003-5171-4ac2-b777-62d94ef8fb7b
```

### Output Example

```bash
# Success
The placeholder VM conversion command was issued.
Task ID: <taskID>
```
