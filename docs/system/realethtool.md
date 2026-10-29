---
sidebar_position: 1
---

# realethtool

### 操作概述

查询网卡状态、统计、驱动及相关诊断信息。

### 命令参数

命令格式：

```bash
acli system realethtool [-S|-i|-a|-g|-m|-t] DEVNAME
```

支持的参数：

本命令为部分参数放通命令，采用封闭式参数白名单（仅列举的参数允许，其余拒绝）。

```bash
-S|--statistics=flag  查看网卡的统计信息
-i|--driver=flag      查看网卡对应的驱动信息
-a|--all=flag         查看网卡的所有信息
-g|--show-ring=flag   查看网卡环形缓冲区参数
-m|--show-module=flag 查看模块信息
-t=flag               执行网卡自检
--show-priv-flags     查看网卡私有标志
-h|--help=flag        显示帮助信息
DEVNAME               必要参数，指定要查看的网卡名（需在白名单接口内），示例：eth0
```

禁止清单：

未列入上述白名单的参数不予放通，包括修改网卡配置的参数。

### 使用示例

```bash
acli system realethtool -g eth0
```

### 结果示例

```bash
# acli system realethtool -g eth0
Ring parameters for eth0:
Pre-set maximums:
RX:             4096
RX Mini:        2048
RX Jumbo:       4096
TX:             4096
Current hardware settings:
RX:             1024
RX Mini:        128
RX Jumbo:       512
TX:             512
```
