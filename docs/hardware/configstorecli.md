---
sidebar_position: 1
---

# configstorecli

### 操作概述

查看、变更主机配置命令

### 命令参数

```bash
config          查看、修改、导出配置
help            查看帮助
migrate-config  配置转换
```

### 使用示例

```bash
acli hardware configstorecli --help
```

### 结果示例

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
