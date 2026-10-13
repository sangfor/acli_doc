---
sidebar_position: 1
---

# arp

### 操作概述

查看 ARP 表（地址解析协议缓存表，只读）。

### 命令参数

本命令为部分只读命令，采用封闭式参数白名单（仅列举的参数允许，其余拒绝）。

```bash
-n|--numeric=flag  可选参数，以数字地址格式显示 ARP 表（不解析主机名），示例：acli system arp -n
```

写参数禁止清单（命中即拒绝）：

```bash
-s|--set <ip> <mac>  添加 ARP 表项（写）
-d|--delete <ip>     删除 ARP 表项（写）
-f|--file <file>     从文件加载 ARP 表项（写）
```

### 使用示例

```bash
acli system arp -n
```

### 结果示例

```bash
# acli system arp -n
Address                  HWtype  HWaddress           Flags Mask            Iface
10.0.0.1                 ether   aa:bb:cc:dd:ee:ff   C                     eth0
10.0.0.2                 ether   11:22:33:44:55:66   C                     eth1
```
