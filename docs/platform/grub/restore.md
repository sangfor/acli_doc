---
sidebar_position: 2
---

# restore

### 操作概述

恢复grub.cfg中的低时延参数

### 命令参数

```bash
-p|--param=string    必要参数，grub参数名，枚举值：nohz_full（低时延参数）
```

### 使用示例

```bash
acli platform grub restore -p nohz_full
```

### 结果示例

```bash
grub参数restore操作成功
```
