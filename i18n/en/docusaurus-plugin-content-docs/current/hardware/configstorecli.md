---
sidebar_position: 1
---

# configstorecli

### Overview

View and modify host configuration commands

### Command Parameters

```bash
config          View, modify, and export configurations
help            Show help
migrate-config  Configuration migration
```

### Usage Example

```bash
acli hardware configstorecli --help
```

### Sample Output

```
HAL Configuration Store CLI - A centralized tool for querying and modifying host configurations stored in the ConfigStore

Usage:
  configstorecli [command]

Available Commands:
  config         View / modify / export Config and DefaultConfig tables
  help           Help about any command
  migrate-config Migrate the SQLite Config table

Flags:
  -h, --help   help for configstorecli

Use "configstorecli [command] --help" for more information about a command.
```
