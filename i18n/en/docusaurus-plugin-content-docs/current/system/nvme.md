---
sidebar_position: 1
---

# nvme

### Overview

Query NVMe devices, identification, status, logs, and features using the permitted read-only subcommands.

### Command Parameters

Command format:

```bash
acli system nvme <subcommand> [arguments]
```

Supported parameters:

This command uses a closed subcommand allowlist. Unlisted subcommands are rejected. Only one subcommand level is supported.

Read-only subcommand allowlist:

```text
list
id-ns
id-ctrl
list-ns
list-subsys
show-regs
error-log
smart-log
effects-log
fw-log
get-feature
get-log
version
help
```

Forbidden arguments:

```text
format
create-ns
delete-ns
attach-ns
detach-ns
reset
sanitize
fw-download
fw-commit
```

Rejected calls return a human-readable reason and a nonzero exit code without exposing sensitive paths or internal implementation details.

### Usage Example

```bash
acli system nvme list
```

### Output Example

When no subcommand is specified:

```text
请指定 nvme 只读子命令（如 list/id-ns/smart-log）
```

Running `acli system nvme list`:

```text
Node                  Generic               SN                   Model                                    Namespace  Usage                      Format           FW Rev
--------------------- --------------------- -------------------- ---------------------------------------- ---------- -------------------------- ---------------- --------
```

This example shows only the table header; no devices were listed by this query.
