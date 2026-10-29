---
sidebar_position: 1
---

# dpdebug

### 操作概述

采集 SDN 数据面的只读诊断信息。

### 命令参数

命令格式：

```bash
acli network dpdebug <collection-type>
```

支持的参数：

```text
<collection-type>    采集类型数字，必须命中封闭式白名单，例如 4
```

禁止清单：

本命令仅放通只读采集，写类参数和子命令显式排除。最多接受 1 个采集类型位置参数，不支持选项；白名单外数字、额外位置参数及未列举选项一律拒绝。

### 使用示例

```bash
acli network dpdebug 4
```

### 结果示例

```text
core-1: 2%, busy: 54871593, idle: 2037796242
```
