---
sidebar_position: 1
---

# get

### 操作概述

查询主机是否在 VS 卷中

### 命令参数

```bash
-h|--hosts=string   必要参数，主机名，多个以英文逗号分隔，示例：host-0050568ec35e 或 host-a,host-b
```

### 使用示例

```bash
acli storage vsmgr host-in-volume get --hosts host-0050568ec35e
```

### 结果示例

1=在卷内且有数据/热备盘，0=不在卷内或无数据/热备盘。

```bash
{"host-0050568ec35e": 1}
```
