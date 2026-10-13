---
sidebar_position: 2
---

# add

### 操作概述

放通指定OS或所有未知OS的CPU/内存热添加

### 命令参数

```bash
-v|--vm-id=string        可选参数，虚拟机 ID（纯数字），从该虚拟机采集的操作系统发行版信息放通 CPU/内存热添加，示例：3535177259949
-o|--os=string           可选参数，操作系统发行版标识(单个OS)，形如 <osname>,<位数>，osname 仅允许字母/数字/空格及 - . _ /，示例：Ubuntu 14,64
-f|--csv-file=string     可选参数，CSV 文件绝对路径，仅允许前缀 /sf/data/local/acli/tmp/ 或 /support/tmp/，示例：/support/tmp/test.csv
-c|--cpu=boolean         可选参数，CPU 热添加能力，true/false；需先指定 --vm-id 或 --os（--csv-file 模式能力由 CSV 每行指定，--all-unknown 模式不支持）；CPU 与 memory 均未指定时，默认放通（true），示例：true
-m|--memory=boolean      可选参数，内存热添加能力，true/false；需先指定 --vm-id 或 --os（--csv-file 模式能力由 CSV 每行指定，--all-unknown 模式不支持）；CPU 与 memory 均未指定时，默认放通（true），示例：true
-a|--all-unknown         可选参数，开启全局兜底：所有未知 OS 均放通 CPU/内存热添加，与 --vm-id/--os/--csv-file 互斥，示例：--all-unknown
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
