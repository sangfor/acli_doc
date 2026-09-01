---
sidebar_position: 4
---

# delete

### Overview

Delete the allow configuration of a specified OS, or disable the global fallback

### Command Parameters

```bash
-o|--os=string      Optional parameter, OS distribution identifier (single OS), in the form <osname>,<bitness>. Example: Ubuntu 14,64
-a|--all-unknown    Optional parameter, disable global fallback: restore to not supporting CPU/memory hot-add for unknown OSes; mutually exclusive with --os. Example: --all-unknown
```

### Usage Example

```bash
# Delete the allow configuration of a specific OS
acli vm hotplug whitelist delete -o "Ubuntu 14,64"

# Disable the global fallback
acli vm hotplug whitelist delete -a
```

### Output Example

```bash
The allow configuration of Ubuntu 14,64 has been deleted
```
