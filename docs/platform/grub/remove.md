---
sidebar_position: 1
---

# remove

### 操作概述

删除grub.cfg中的低时延参数

### 命令参数

```bash
-p|--param=string    必要参数，grub参数名，枚举值：nohz_full（低时延参数）
```

### 使用示例

```bash
acli platform grub remove -p nohz_full
```

### 结果示例

```bash
grub参数remove操作成功
```
