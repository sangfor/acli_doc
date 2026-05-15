---
sidebar_position: 1
---

# skip

### 操作概述

跳过sagaflow分支回滚

### 命令参数

```bash
-g|--group=string     必要参数，分组名称，示例：test-api-demo-001
-b|--branch=string    必要参数，分支名称，示例：01
```

### 使用示例

```bash
acli vm sagaflow branch rollback skip -g 'test-api-demo-001' -b '01'
```

### 结果示例

```bash
{"after":"Set rollbacking branch succeed completed"}
```
