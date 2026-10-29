---
sidebar_position: 1
---

# iscsiadm

### 操作概述

查询 iSCSI 会话、发现目标及节点信息，仅放通指定的只读参数组合。

### 命令参数

命令格式：

```bash
acli system iscsiadm -m session
acli system iscsiadm -m discovery -t st -p <IP:Port>
acli system iscsiadm -m discovery -t sendtargets -p <IP:Port>
acli system iscsiadm -m node
acli system iscsiadm -m node -o show
```

支持的参数：

本命令采用封闭式参数白名单（未列举即拒绝）。仅支持下列 POSIX 短选项组合，不放通其他选项或写操作。

```text
-m session      查询当前 iSCSI 会话
-m discovery    发现 iSCSI 目标，需配合 -t 和 -p
-t st           SendTargets 发现类型（也支持 sendtargets）
-p <IP:Port>    指定目标门户的 IP 地址和端口
-m node         查询 iSCSI 节点信息
-o show         显示节点信息，node 模式下仅允许此操作
```

禁止清单：

```text
-o new
-o delete
-o update
-m iface -o update
```

`iface` 模式和其他白名单外参数组合同样拒绝，不因单个选项出现在允许组合中而单独放通。

### 使用示例

```bash
acli system iscsiadm -m session
```

### 结果示例

```text
iscsiadm: No active sessions.
```
