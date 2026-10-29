---
sidebar_position: 1
---

# rpcinfo

### 操作概述

查询 RPC 服务的注册信息，包括程序号、版本、传输协议、地址和服务名称。

### 命令参数

命令格式：

```bash
acli system rpcinfo
acli system rpcinfo [options] [arguments]
```

支持的参数：

本命令为部分只读命令，采用封闭式参数白名单（仅列举的参数允许，其余拒绝）。不指定参数时查询本机 RPC 注册信息。

只读参数白名单：

```text
-a -b -l -m -n -p -s -t -T -u
```

各选项所需的地址、主机、程序号、版本号等参数应按对应查询方式提供。

禁止清单：

```text
-d prognum versnum    删除指定 RPC 程序在 rpcbind 中的注册项，属于写操作，拒绝执行
```

合并短选项按字符逐位检查，只要包含 `d` 即拒绝。

`-Z`（大写 Z）仅为提取 usage 的探针，不属于正常只读参数集，不予放通。

### 使用示例

```bash
acli system rpcinfo
```

### 结果示例

```text
   program version netid     address                service    owner
    100000    4    tcp6      ::.0.111               portmapper superuser
    100000    3    tcp6      ::.0.111               portmapper superuser
    100000    4    udp6      ::.0.111               portmapper superuser
    100000    3    udp6      ::.0.111               portmapper superuser
    100000    4    tcp       0.0.0.0.0.111          portmapper superuser
    100000    3    tcp       0.0.0.0.0.111          portmapper superuser
    100000    2    tcp       0.0.0.0.0.111          portmapper superuser
    100000    4    udp       0.0.0.0.0.111          portmapper superuser
    100000    3    udp       0.0.0.0.0.111          portmapper superuser
    100000    2    udp       0.0.0.0.0.111          portmapper superuser
    100000    4    local     /var/run/rpcbind.sock  portmapper superuser
    100000    3    local     /var/run/rpcbind.sock  portmapper superuser
    100024    1    udp       0.0.0.0.150.80         status     superuser
    100024    1    tcp       0.0.0.0.150.80         status     superuser
    100024    1    udp6      ::.150.80              status     superuser
    100024    1    tcp6      ::.150.80              status     superuser
    100003    3    tcp       0.0.0.0.8.1            nfs        superuser
    100005    3    tcp       0.0.0.0.150.65         mountd     superuser
    100005    1    tcp       0.0.0.0.150.66         mountd     superuser
```
