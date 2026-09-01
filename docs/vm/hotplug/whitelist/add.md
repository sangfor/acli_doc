---
sidebar_position: 2
---

# add

### 操作概述

放通指定OS或所有未知OS的CPU/内存热添加

### 命令参数

```bash
-v|--vm-id=string        可选参数，虚拟机id，从该虚拟机采集的操作系统发行版信息放通CPU/内存热添加，示例：3535177259949
-o|--os=string           可选参数，操作系统发行版标识(单个OS)，形如 <osname>,<位数>，示例：Ubuntu 14,64
-f|--csv-file=string     可选参数，CSV 文件绝对路径（不支持相对路径），表头 os_distribution,is_supported_cpu_hotplug,is_supported_memory_hotplug；host 端把文件写入 ~/tmp/ 或 /sf/data/local/acli/tmp/ 后传任意可访问绝对路径即可，示例：/support/tmp/test.csv
-c|--cpu=boolean         可选参数，CPU热添加能力，true/false；需先指定 --vm-id 或 --os 使用（--csv-file 模式能力由 CSV 每行指定，--all-unknown 模式不支持）；cpu 与 memory 均未指定时，默认放通（true），示例：true
-m|--memory=boolean      可选参数，内存热添加能力，true/false；需先指定 --vm-id 或 --os 使用（--csv-file 模式能力由 CSV 每行指定，--all-unknown 模式不支持）；cpu 与 memory 均未指定时，默认放通（true），示例：true
-a|--all-unknown         可选参数，开启全局兜底：所有未知OS均放通CPU/内存热添加，与 --vm-id/--os/--csv-file 互斥，示例：--all-unknown
```

### 使用示例

```bash
# 放通指定 OS 的 CPU/内存热添加
acli vm hotplug whitelist add -o "Ubuntu 14,64" --cpu true --memory true

# 从指定虚拟机采集的 OS 信息放通热添加
acli vm hotplug whitelist add -v 3535177259949

# 通过 CSV 文件批量放通
acli vm hotplug whitelist add -f /support/tmp/test.csv

# 开启全局兜底：所有未知 OS 均放通
acli vm hotplug whitelist add -a
```

### 结果示例

```bash
已添加 Ubuntu 14,64
```
