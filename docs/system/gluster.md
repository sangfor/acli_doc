---
sidebar_position: 1
---

# gluster

### 操作概述

查询 Gluster 卷信息或卷列表（只读）。

### 命令参数

命令格式：

```bash
acli system gluster v i
acli system gluster v list
```

支持的参数：

本命令采用封闭式子命令白名单，仅允许以下两种调用形式：

```text
v i       gluster volume info 的简写，查询卷信息
v list    gluster volume list 的简写，查询卷列表
```

禁止清单：

子命令参数必须恰好为 2 个 token，并精确匹配 `v i` 或 `v list`。其他子命令、完整拼写形式、额外参数和选项一律拒绝。

拒绝时返回人类可读的原因及非零退出码，不泄露敏感路径或内部实现细节。

### 使用示例

```bash
acli system gluster v i
```

### 结果示例

执行 `acli system gluster v i`，当前没有卷时输出：

```text
No volumes present
```
