---
sidebar_position: 3
---

# set

### Overview

Modify the CPU/memory hot-add capability for a specified OS

### Command Parameters

```bash
-o|--os=string        Required parameter, OS distribution identifier (single OS), in the form <osname>,<bitness>. Example: Ubuntu 14,64
-c|--cpu=boolean      Optional parameter, CPU hot-add capability, true/false; requires --os to be specified first (--os is required); if not specified, the current value is kept. Example: true
-m|--memory=boolean   Optional parameter, memory hot-add capability, true/false; requires --os to be specified first (--os is required); if not specified, the current value is kept. Example: false
```

### Usage Example

```bash
# Modify the CPU hot-add capability of a specific OS
acli vm hotplug whitelist set -o "Ubuntu 14,64" -c true

# Modify the memory hot-add capability of a specific OS
acli vm hotplug whitelist set -o "Ubuntu 14,64" -m false

# Modify both CPU and memory hot-add capabilities
acli vm hotplug whitelist set -o "Ubuntu 14,64" -c true -m true
```

### Output Example

```bash
Ubuntu 14,64 has been modified: CPU hot-add supported
```
