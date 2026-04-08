---
sidebar_position: 7
---

# shell

### 操作概述

程序内置了一些脚本文件，当环境中不存在时可执行

### 命令参数

```bash
[script]                     指定要执行的脚本名称。脚本需要解压后才能使用，用-e参数解压脚本。
-e|--extract                 解压内置脚本到配置目录，目录位置：/sf/data/local/performance_tools/scripts/
```

### 使用示例

```bash
# 示例1：解压内置脚本到配置目录
acli performance_tools shell -e

# 示例2：显示帮助信息
acli performance_tools shell vm_isolation.sh
```

### 结果示例

```bash
# acli performance_tools shell vm_isolation.sh
usage: /sf/data/local/performance_tools/vm_isolation.sh option
  isolate vmid pcpu_str [inc_service]             指定PCPU范围给虚拟机独占，pcpu_str格式为: 1-3,5
  isolate only_pcpu pcpu_str                      只指定隔离pcpu
  unisolate vmid|only_pcpu                        取消某台虚拟机或者only_pcpu的独占
  isolated_list                                   获取独占的虚拟机列表

# acli performance_tools shell -e
成功解压脚本：sfd_performance_handling.sh 到 /sf/data/local/performance_tools/scripts/sfd_performance_handling.sh
成功解压脚本：vm_isolation.sh 到 /sf/data/local/performance_tools/scripts/vm_isolation.sh
成功解压脚本：sfd_mem_tools_new.sh 到 /sf/data/local/performance_tools/scripts/sfd_mem_tools_new.sh
成功解压脚本：get_hw_cti.sh 到 /sf/data/local/performance_tools/scripts/get_hw_cti.sh
成功解压脚本：pidstat_x86 到 /sf/data/local/performance_tools/scripts/pidstat_x86
所有脚本已成功解压到：/sf/data/local/performance_tools/scripts
```
