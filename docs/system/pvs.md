---
sidebar_position: 1
---

# pvs

### 操作概述

查询 LVM 物理卷信息。

### 命令参数

命令格式：

```bash
acli system pvs [options] [PV|Tag ...]
```

`PV|Tag ...` 为可选参数，用于指定物理卷或标签。不指定时查询物理卷列表。

工具支持的选项见下方帮助输出，包括显示字段、筛选、排序、分段信息及报告格式等选项。

### 使用示例

```bash
acli system pvs -h
```

### 结果示例

执行 `acli system pvs -h` 返回以下帮助信息：

```text
  pvs - Display information about physical volumes

  pvs
        [ -a|--all ]
        [ -o|--options String ]
        [ -S|--select String ]
        [ -O|--sort String ]
        [    --segments ]
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
        [ PV|Tag ... ]

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
