---
sidebar_position: 2
---

# set

### 操作概述

修改虚拟机自定义 SMBIOS 厂商信息（manufacturer）及启用开关（冷编辑，仅支持关机状态下修改；运行中的虚拟机将被拒绝）

### 命令参数

```bash
-v|--vm-id=string          必要参数，虚拟机ID，示例：614182240912
-m|--manufacturer=string   必要参数，目标厂商信息，长度 1-64 字符（仅允许可打印 ASCII 字符，不支持中文字符、换行及 tab 等非可打印字符）；逗号原样输入（如 VMware, Inc.），由代码层转义；建议避免使用等号 '='，可能导致 QEMU 解析异常；启用自定义时必须填写该值，示例：HPE
-e|--enabled=boolean       必要参数，是否启用自定义 SMBIOS 厂商信息，枚举值：true（启用自定义值生效）、false（使用默认 sangfor 逻辑，但保留 manufacturer 旧值不清空），示例：true
```

### 使用示例

```bash
acli vm advcfg smbios set -v 614182240912 -m HPE -e true
acli vm advcfg smbios set -v 614182240912 -m "VMware, Inc." -e true
```

### 结果示例

```bash
您确定要执行这个操作? (y[es]/n[o]): y
enabledAfter: true
enabledBefore: false
manufacturerAfter: HPE
manufacturerBefore: null
taskID: host-005056b2894b:280998:1760441353:6913569233831
vmID: 614182240912
```