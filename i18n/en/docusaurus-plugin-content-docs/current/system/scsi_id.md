---
sidebar_position: 1
---

# scsi_id

### Overview

Query SCSI device identification information using read-only operations with controlled device paths.

### Command Parameters

Command format:

```bash
acli system scsi_id --device=<device> [options]
```

Supported parameters:

This command uses a closed argument allowlist. Unlisted options are rejected. It has no write capability.

```text
-g|--whitelisted=flag       Treat the device as whitelisted for querying
-u|--replace-whitespace=flag Replace whitespace in the output
-x|--export=flag            Export information as key-value pairs
-d|--device=string          Specify the device path, subject to path access controls
-p|--page=string            Specify the VPD page to query
-s|--sg-version=string      Specify the SG interface version
```

Value-taking options support the `=` form, for example, `--device=/dev/sda`. Specify the device through `-d/--device`.

Forbidden arguments:

Bare positional arguments and unlisted options are rejected.

### Usage Example

```bash
acli system scsi_id --device=/dev/sda -g
```

### Output Example

```text
36000c295698055ee2ad7475a1ee499b2
```
