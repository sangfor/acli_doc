---
sidebar_position: 1
---

# hostcli

### 操作概述

hostcli 是一款用于管理和监控主机硬件的命令行工具。它提供查询硬件信息的功能，可对磁盘、存储控制器、CPU 等各类硬件组件进行操作。

### 命令参数

```bash
hardware    硬件相关操作
help        查看帮助
storage     存储相关操作
system      系统相关操作
version     打印版本信息并退出
```

### 使用示例

```bash
acli hardware hostcli --help
```

### 结果示例

```
hostcli is a command line tool that allows you to manage and monitor host hardware.
It provides functionality to query hardware information and perform operations on various
hardware components like disks, storage controllers, and CPUs.

Usage:
  hostcli [command]

Available Commands:
  hardware    Hardware related operations
  help        Help about any command
  storage     Storage related operations
  system      System related operations
  version     Print version information and quit

Flags:
      --debug   enable debug mode

Use "hostcli [command] --help" for more information about a command.
```
