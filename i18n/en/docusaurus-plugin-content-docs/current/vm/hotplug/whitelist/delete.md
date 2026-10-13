---
sidebar_position: 4
---

# delete

### Overview

Delete the configuration of allowing specified OSes or disable the global default policy

### Command Parameters

```bash
-o|--os=string      Optional parameter, OS distribution identifier (single OS), format: <osname>,<bit>. osname can contain only letters, digits, spaces, and special characters ( - . _ /). Example: Ubuntu 14,64
-a|--all-unknown    Optional parameter, disable global default policy: Restore to not supporting CPU/memory hot-add for unknown OSes. It is mutually exclusive with --os. Example: --all-unknown
```

### Usage Example

```bash
# Delete the allow configuration of a specific OS
acli vm hotplug whitelist delete -o "Ubuntu 14,64"

# Disable the global default policy
acli vm hotplug whitelist delete -a
```

### Output Example

```bash
Deleted the configuration of allowing hot-add for Ubuntu 14,64.
```
