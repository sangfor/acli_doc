---
sidebar_position: 1
---

# import

### Overview

Import VM configuration from the replica datastore by reading the conf file of the source VM, generating disk mappings according to the user-specified datastore mapping, and calling the vmman import-config API to issue an import command.

### Command Parameters

```bash
-s|--source-vm-id=string        Required parameter, Source VM ID. Example: 6882173957870
-c|--cfgstorage-id=string       Required parameter, Datastore ID of source VM configuration. Example: 1SANGFOR_ASAN-003-5171-4ac2-b777-62d94ef8fb7b
-t|--target-vm-id=string        Target VM ID (optional). Example: 9876543210
-m|--storage-map=string         Required parameter, Datastore mapping format: src=<source datastore ID>, dst=<destination datastore ID>. Multiple mappings must be separated by semicolons. Example: src=1SANGFOR_ASAN-003-5171-4ac2-b777-62d94ef8fb7b,dst=1SANGFOR_ASAN-003-5171-4ac2-b777-62d94ef8fb7c;src=pool_a,dst=pool_b
```

### Usage Example

```bash
acli vm dr config import -s 6882173957870 -c 1SANGFOR_ASAN-003-5171-4ac2-b777-62d94ef8fb7b -m src=1SANGFOR_ASAN-003-5171-4ac2-b777-62d94ef8fb7b,dst=1SANGFOR_ASAN-003-5171-4ac2-b777-62d94ef8fb7c
```

### Output Example

```bash
# Success
The VM configuration import command was issued.
Task ID: <taskID>
```
