---
sidebar_position: 1
---

# vs_check_vms_poly

### Overview

Perform read-only checks of virtual machine disk POLY status.

### Command Parameters

Command format:

```bash
acli storage asan vs_check_vms_poly [options]
```

Supported parameters:

This command uses a closed argument allowlist. Only read-only checks are permitted. Write options, write subcommands, and unlisted arguments are rejected.

Boolean option allowlist:

```text
-a|--all
-d|--detail
-p|--poly
```

Value-taking option allowlist:

```text
-v|--vmid=string    Specify a virtual machine ID
-f|--file=string    Specify a file
-g|--gfid=string    Specify a GFID
-t|--tid=string     Specify a TID
-n|--name=string    Specify a name
```

Both short options with values and GNU long options using `=` are supported, for example, `-v 343999323256` or `--vmid=343999323256`. All positional arguments are rejected; specify check targets through options.

Forbidden arguments:

Reject positional arguments, write options, write subcommands, and unlisted options.

### Usage Example

```bash
acli storage asan vs_check_vms_poly -v 343999323256
```

### Output Example

```text
--------------------------------------------------------------------------------------------------------------------------
hci-6.11.6 343999323256
vm-disk-3.qcow2 POLY 200.201.38.27
vm-disk-2.qcow2 POLY 200.201.38.27
vm-disk-4.qcow2 POLY 200.201.38.27
vm-disk-1.qcow2 POLY 200.201.38.27
--------------------------------------------------------------------------------------------------------------------------
```
