---
sidebar_position: 1
---

# lvscan

### 操作概述

列出所有卷组中的逻辑卷。

### 命令参数

命令格式：

```bash
acli system lvscan [options]
```

工具支持的选项见下方帮助输出，包括显示全部逻辑卷、块设备信息和报告格式等选项。

### 使用示例

```bash
acli system lvscan -h
```

### 结果示例

执行 `acli system lvscan -h` 返回以下帮助信息：

```text
  lvscan - List all logical volumes in all volume groups

  lvscan
        [ -a|--all ]
        [ -b|--blockdevice ]
        [    --ignorelockingfailure ]
        [    --readonly ]
        [    --reportformat basic|json|json_std ]
        [ COMMON_OPTIONS ]

  Common options for lvm:
        [ -d|--debug ]
        [ -h|--help ]
        [ -q|--quiet ]
        [ -v|--verbose ]
        [ -y|--yes ]
        [ -t|--test ]
        [    --commandprofile String ]
        [    --config String ]
        [    --driverloaded y|n ]
        [    --nolocking ]
        [    --lockopt String ]
        [    --longhelp ]
        [    --profile String ]
        [    --version ]
        [    --devicesfile String ]
        [    --devices PV ]
        [    --nohints ]
        [    --journal String ]

  Use --longhelp to show all options and advanced commands.
```
