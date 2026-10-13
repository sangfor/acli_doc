---
sidebar_position: 1
---

# clear

### 操作概述

清除指定节点上指定 vendor/product 的 device 级 multipath 自定义配置。

### 命令参数

```bash
-n|--hostname=string    可选参数，目标主机名，缺省为当前节点，示例：host-xxxx
-v|--vendor=string     必要参数，multipath.conf vendor 字段，示例：DellEMC
-p|--product=string    必要参数，multipath.conf product 字段，示例：PowerStore
```

### 使用示例

```bash
acli system multipathconfig devicepolicy clear -n host-xxxx -v DellEMC -p PowerStore
```

### 结果示例

```bash
affected_storages:
  [0]: 3648bd4a100fa95b6550a2d9c000002ac
  [1]: 3648bd4a100fa95b6550a2d9c000002ad
```
