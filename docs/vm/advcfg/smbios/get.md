---
sidebar_position: 1
---

# get

### 操作概述

查询虚拟机自定义 SMBIOS 厂商信息（manufacturer）及其启用开关状态

### 命令参数

```bash
-v|--vm-id=string  必要参数，虚拟机ID，示例：614182240912
```

### 使用示例

```bash
acli vm advcfg smbios get -v 614182240912
```

### 结果示例

```bash
enabled: true
manufacturer: HPE
vmID: 614182240912
```