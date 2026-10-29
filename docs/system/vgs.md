---
sidebar_position: 1
---

# vgs

### 操作概述

查询 LVM 卷组信息。

### 命令参数

命令格式：

```bash
acli system vgs [options] [VG|Tag ...]
```

`VG|Tag ...` 为可选参数，用于指定卷组或标签。不指定时查询卷组列表。

工具支持的选项见下方帮助输出，包括显示字段、筛选、排序及报告格式等选项。

### 使用示例

```bash
acli system vgs -h
```

### 结果示例

执行 `acli system vgs -h` 返回以下帮助信息：

```text
  vgs - Display information about volume groups

  vgs
        [ -a|--all ]
        [ -o|--options String ]
        [ -S|--select String ]
        [ -O|--sort String ]
        [    --aligned ]
        [    --binary ]
        [    --configreport log|vg|lv|pv|pvseg|seg ]
        [    --foreign ]
        [    --ignorelockingfailure ]
        [    --logonly ]
        [    --nameprefixes ]
        [    --noheadings ]
        [    --nosuffix ]
        [    --readonly ]
        [    --reportformat basic|json|json_std ]
        [    --rows ]
        [    --separator String ]
        [    --shared ]
        [    --unbuffered ]
        [    --units [Number]r|R|h|H|b|B|s|S|k|K|m|M|g|G|t|T|p|P|e|E ]
        [    --unquoted ]
        [ COMMON_OPTIONS ]
        [ VG|Tag ... ]

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
