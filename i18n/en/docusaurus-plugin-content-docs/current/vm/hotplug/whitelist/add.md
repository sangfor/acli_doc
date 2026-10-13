---
sidebar_position: 2
---

# add

### Overview

Allow CPU/memory hot-add for specified OSes or all unknown OSes

### Command Parameters

```bash
-v|--vm-id=string        Optional parameter, VM ID, which is used to allow CPU/memory hot-add based on the OS distribution information collected from this VM. Example: 3535177259949
-o|--os=string           Optional parameter, OS distribution identifier (single OS), format: <osname>,<bit>. osname can contain only letters, digits, spaces, and special characters ( - . _ /). Example: Ubuntu 14,64
-f|--csv-file=string     Optional parameter, absolute path of CSV file, which can only start with /sf/data/local/acli/tmp/ or /support/tmp/. Example: /support/tmp/test.csv
-c|--cpu=boolean         Optional parameter, CPU hot-add capability (true/false); must specify --vm-id or --os first (--csv-file mode capability is specified by each row of CSV file; this parameter is not supported by --all-unknown mode). If neither CPU nor memory is specified, the default value is true (allow hot-add). Example: true
-m|--memory=boolean      Optional parameter, memory hot-add capability (true/false); must specify --vm-id or --os first (--csv-file mode capability is specified by each row of CSV file; this parameter is not supported by --all-unknown mode). If neither CPU nor memory is specified, the default value is true (allow hot-add). Example: true
-a|--all-unknown         Optional parameter, enable global default policy: CPU/memory hot-add is allowed for all unknown OSes. It is mutually exclusive with --vm-id/--os/--csv-file. Example: --all-unknown
```

### Usage Example

```bash
# Allow CPU/memory hot-add for a specific OS
acli vm hotplug whitelist add -o "Ubuntu 14,64" -c true -m true

# Allow hot-add based on the OS information collected from a specific VM
acli vm hotplug whitelist add -v 3535177259949

# Batch allow via a CSV file
acli vm hotplug whitelist add -f /support/tmp/test.csv

# Enable global default policy: allow all unknown OSes
acli vm hotplug whitelist add -a
```

### Output Example

```bash
Added: Ubuntu 14,64
```
