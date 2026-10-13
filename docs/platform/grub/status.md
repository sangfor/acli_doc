---
sidebar_position: 3
---

# status

### 操作概述

查询grub.cfg低时延参数状态

### 命令参数

```bash
-p|--param=string    必要参数，grub参数名，枚举值：nohz_full（低时延参数）
```

### 使用示例

```bash
acli platform grub status -p nohz_full
```

### 结果示例

```bash
=== nohz_full status ===
current grub.cfg nohz_full=    : 2-3
state file                     : /sf/etc/grub_ctl/nohz_full.state
  saved fingerprint            : 5.10.0-1_xxx
  current fingerprint          : 5.10.0-1_xxx
  fingerprint changed          : no
  saved value                  : 2-3
  saved action                 : removed
```
