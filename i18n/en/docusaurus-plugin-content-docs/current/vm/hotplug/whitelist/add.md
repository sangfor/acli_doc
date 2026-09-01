---
sidebar_position: 2
---

# add

### Overview

Allow CPU/memory hot-add for a specified OS or all unknown OSes

### Command Parameters

```bash
-v|--vm-id=string        Optional parameter, VM ID. Allow CPU/memory hot-add based on the OS distribution information collected from this VM. Example: 3535177259949
-o|--os=string           Optional parameter, OS distribution identifier (single OS), in the form <osname>,<bitness>. Example: Ubuntu 14,64
-f|--csv-file=string     Optional parameter, absolute path of the CSV file (relative paths are not supported), with headers os_distribution,is_supported_cpu_hotplug,is_supported_memory_hotplug; write the file to ~/tmp/ or /sf/data/local/acli/tmp/ on the host side and pass any accessible absolute path. Example: /support/tmp/test.csv
-c|--cpu=boolean         Optional parameter, CPU hot-add capability, true/false; requires --vm-id or --os to be specified first (in --csv-file mode the capability is specified per CSV row; not supported in --all-unknown mode); if neither cpu nor memory is specified, it defaults to allowed (true). Example: true
-m|--memory=boolean      Optional parameter, memory hot-add capability, true/false; requires --vm-id or --os to be specified first (in --csv-file mode the capability is specified per CSV row; not supported in --all-unknown mode); if neither cpu nor memory is specified, it defaults to allowed (true). Example: true
-a|--all-unknown         Optional parameter, enable global fallback: allow CPU/memory hot-add for all unknown OSes; mutually exclusive with --vm-id/--os/--csv-file. Example: --all-unknown
```

### Usage Example

```bash
# Allow CPU/memory hot-add for a specific OS
acli vm hotplug whitelist add -o "Ubuntu 14,64" -c true -m true

# Allow hot-add based on the OS information collected from a specific VM
acli vm hotplug whitelist add -v 3535177259949

# Batch allow via a CSV file
acli vm hotplug whitelist add -f /support/tmp/test.csv

# Enable global fallback: allow all unknown OSes
acli vm hotplug whitelist add -a
```

### Output Example

```bash
Ubuntu 14,64 has been added
```
