---
sidebar_position: 1
---

# get

### 操作概述

查询单张虚拟机网卡类型（冷编辑查询，VM 开机/关机态均可查询单张网卡详情）。

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机ID，必须是纯数字组合，示例：4133790374747
-n|--nic-id=string   必要参数，单张网卡ID（UUID 格式，即 conf 文件中的 iface_id 字段），示例：34a89548-2923-4a87-93ab-ee71846fb6ba
```

### 使用示例

```bash
acli vm advcfg nic-type get --vm-id 4133790374747 --nic-id 34a89548-2923-4a87-93ab-ee71846fb6ba
```

### 结果示例

```bash
nics:
  [0]:
    macAddress: FE:FC:FE:0D:5D:88
    model: e1000
    nicID: 34a89548-2923-4a87-93ab-ee71846fb6ba
    nicName: net0
```
