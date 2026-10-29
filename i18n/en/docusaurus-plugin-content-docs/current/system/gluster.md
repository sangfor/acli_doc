---
sidebar_position: 1
---

# gluster

### Overview

Query Gluster volume information or list volumes (read-only).

### Command Parameters

Command format:

```bash
acli system gluster v i
acli system gluster v list
```

Supported parameters:

This command uses a closed subcommand allowlist. Only the following two forms are permitted:

```text
v i       Abbreviation of gluster volume info; query volume information
v list    Abbreviation of gluster volume list; list volumes
```

Forbidden arguments:

Exactly two subcommand tokens are required, matching either `v i` or `v list`. All other subcommands, fully spelled-out forms, extra arguments, and options are rejected.

Rejected calls return a human-readable reason and a nonzero exit code without exposing sensitive paths or internal implementation details.

### Usage Example

```bash
acli system gluster v i
```

### Output Example

Running `acli system gluster v i` when no volumes are present returns:

```text
No volumes present
```
