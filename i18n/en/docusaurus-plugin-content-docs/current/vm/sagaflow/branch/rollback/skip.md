---
sidebar_position: 1
---

# skip

### Overview

Skip sagaflow branch rollback

### Command Parameters

```bash
-g|--group=string     Required parameter, group name, example: test-api-demo-001
-b|--branch=string    Required parameter, branch name, example: 01
```

### Usage Example

```bash
acli vm sagaflow branch rollback skip -g 'test-api-demo-001' -b '01'
```

### Output Example

```bash
{"after":"Set rollbacking branch succeed completed"}
```
