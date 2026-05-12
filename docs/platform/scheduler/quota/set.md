---
sidebar_position: 2
---

# set

### 操作概述

修改调度器配额信息

### 命令参数

```bash
--params=object                      必要参数，配额参数，包含resourceType和配额值
--params.clusterQuota=integer        集群级配额上限
--params.faultToleranceQuota=integer 故障容错配额
--params.nodeQuota=integer           单主机级配额上限
--params.resourceType=string         必要参数，资源类型
```

### 使用示例

```bash
acli platform scheduler quota set --params.resourceType computeOperate --params.nodeQuota 35
```

### 结果示例

```bash
nodeQuota: 10
resourceType: computeOperate
```
