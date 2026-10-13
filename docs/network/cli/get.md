---
sidebar_position: 1
---

# get

### 操作概述

在 vn-agent 容器内执行 SDN cli 的只读 show 查询命令

### 命令参数

```bash
<show-subcommand>  必要参数，SDN cli 支持的只读子命令，可通过 --list 参数获取所有子命令
--list=flag        列出 SDN cli 支持的所有子命令
```

### 使用示例

```bash
acli network cli get arp
```

```bash
acli network cli get --list
```

### 结果示例

```bash
# acli network cli get arp
ARP entries:
IP               MAC                VLAN  Interface
10.10.1.2        00:0c:29:56:b7:a6  1     eth0
10.10.1.3        00:0c:29:56:aa:bb  1     eth0
```
