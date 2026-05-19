---
sidebar_position: 1
---

# list

### Overview

Display all aCLI commands

### Command Parameters
```bash
-c|--command-filter=string        Display only commands whose names contain the specified string, Example: list
-d|--description-filter=string    Display only commands whose descriptions contain the specified string, Example: aCLI command
-n|--namespace-filter=string      Display only commands whose namespaces contain the specified string, Example: command
```

### Usage Example

```bash
# Query All Command Information
acli command list

Query commands with namespace containing 'host'
acli command list -n host
```

### Output Example

```bash
Namespace | Command | Description
--------------------------------------------  -----------  ------------------------------------------
hardware.disk.smartinfo                       get          Retrieve all SMART information of the hard disk
hardware.cpu.info                             get          Get CPU information from hardware
......
```