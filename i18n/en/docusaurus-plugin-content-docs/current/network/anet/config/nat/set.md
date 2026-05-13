---
sidebar_position: 1
---

# set

### Overview

Adjust NAT entry restrictions

### Command Parameters
```bash
-m|--max-size=integer    Required parameter, nat entry configuration specification, 65536(min), 131072(max), Enum values: 65536,131072
```

### Usage Example

```bash
acli network anet config nat set -m 65536
```

### Output Example

```bash
Command executed successfully.
```