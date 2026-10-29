---
sidebar_position: 1
---

# dpdebug

### Overview

Collect read-only SDN dataplane diagnostic information.

### Command Parameters

Command format:

```bash
acli network dpdebug <collection-type>
```

Supported parameters:

```text
<collection-type>    Numeric collection type; must match the closed allowlist, for example, 4
```

Forbidden arguments:

Only read-only collection is permitted; write parameters and subcommands are explicitly excluded. At most one collection-type positional argument is accepted. Options are not supported. Numbers outside the allowlist, extra positional arguments, and unlisted options are rejected.

### Usage Example

```bash
acli network dpdebug 4
```

### Output Example

```text
core-1: 2%, busy: 54871593, idle: 2037796242
```
