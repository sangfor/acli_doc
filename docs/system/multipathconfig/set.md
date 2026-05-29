---
sidebar_position: 1
---

# set

### 操作概述

修改multipath多路径策略

### 命令参数

```bash
-w|--wwid=string                     必要参数，逻辑存储ID，示例：3648bd4a100fa95b6550a2d9c000002ac
-n|--nodes=string                    必要参数，主机ID列表，多个节点逗号分隔，示例：host-0050568eefd7,host-a416e704e387
-g|--path-grouping-policy=string     必要参数，路径分组策略，failover(主备模式)，multibus(负载均衡模式)，group_by_prio(按优先级分组)，group_by_serial(按序列号分组)，group_by_node_name(按节点名分组)
```

### 使用示例

```bash
acli system multipathconfig set -w 3648bd4a100fa95b6550a2d9c000002ac -n host-0050568eefd7,host-a416e704e387 -g failover
```

### 结果示例

```bash
UPID:host-005056b22c8d:00276CFF:BD680A:6A18ED61:设置多路径策略::admin@vtp:
```
