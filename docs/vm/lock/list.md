---
sidebar_position: 1
---

# list

### 操作概述

获得特定目录下和vm-id有关的锁文件

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机id，示例：2848367193475
```

### 使用示例

```bash
acli vm lock list -v 1072335336316
```

### 结果示例

```bash
# 获得下列目录下以vm-id开头的文件和目录
# "/var/lock/flag_dir/"
# "/cfs/vm_tmp_status/flag_dir/"
# "/cfs/priv/lock/"
1072335336316_vm
1072335336316_p
1072335336316_lock_file
```
