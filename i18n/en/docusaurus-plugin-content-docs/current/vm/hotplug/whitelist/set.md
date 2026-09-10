---
sidebar_position: 3
---

# set

### Overview

Modify the capability of allowing CPU/memory hot-add for the specified OS

### Command Parameters

```bash
-o|--os=string        Required parameter, OS distribution identifier (single OS), format: <osname>,<bit>. osname can contain only letters, digits, spaces, and special characters ( - . _ /). Example: Ubuntu 14,64
-c|--cpu=boolean      Optional parameter, CPU hot-add capability (true/false); must specify --os first (--os is required), and keep the original value if not passed in. Example: true
-m|--memory=boolean   Optional parameter, memory hot-add capability (true/false); must specify --os first (--os is required), and keep the original value if not passed in. Example: false
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
Modified: Ubuntu 14,64: CPU hot-add: Supported
```
