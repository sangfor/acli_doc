---
sidebar_position: 1
---

# route

### 操作概述

查看系统路由表（只读）。

### 命令参数

本命令为部分只读命令，采用封闭式参数白名单（仅列举的参数允许，其余拒绝）。

```bash
-n|--numeric=flag   可选参数，以数字地址格式显示路由（不解析主机名）
-e|--extend=flag    可选参数，详细显示路由
-ee                 可选参数，详细显示路由（-e 的加重形式）
（无参数）        可选参数，查询默认路由表
-A|--family=string  可选参数，指定地址族查询（inet/ipv6 等），示例：-A inet
-C|--cache=flag     可选参数，查询路由缓存
```

写参数禁止清单（命中即拒绝）：

```bash
add                    添加路由（写）
del                    删除路由（写）
flush                  清空路由缓存（写）
-i <dev> add/del       指定网络接口添加/删除路由（写）
-host/-net 配合 add/del  指定主机/网络添加/删除路由（写）
```

### 使用示例

```bash
acli system route -n
```

### 结果示例

```bash
# acli system route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.0.0.1        0.0.0.0         UG    0      0        0 eth0
10.0.0.0        0.0.0.0         255.255.255.0   U     100    0        0 eth0
```
