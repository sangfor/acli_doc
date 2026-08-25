---
sidebar_position: 1
---

# list

### 操作概述

列出虚拟机网卡类型（冷编辑查询，VM 开机/关机态均可查询；不传 `--nic-id` 返回该 VM 全部网卡，传逗号分隔的多值返回匹配集合，任一不匹配整体报错）。

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机ID，必须是纯数字组合，示例：4133790374747
-n|--nic-id=string   可选参数，网卡ID（UUID 格式），支持逗号分隔多值（0-n 个），不传返回该 VM 全部网卡，示例：34a89548-2923-4a87-93ab-ee71846fb6ba,a05805f9-7e8b-44fe-91a7-a84a3b83eb50
```

### 使用示例

```bash
acli vm advcfg nic-type list --vm-id 4133790374747
acli vm advcfg nic-type list --vm-id 4133790374747 --nic-id 34a89548-2923-4a87-93ab-ee71846fb6ba,a05805f9-7e8b-44fe-91a7-a84a3b83eb50
```

### 结果示例

```bash
nics:
  [0]:
    macAddress: FE:FC:FE:0D:5D:88
    model: e1000
    nicID: 34a89548-2923-4a87-93ab-ee71846fb6ba
    nicName: net0
  [1]:
    macAddress: FE:FC:FE:D3:B0:44
    model: e1000
    nicID: a05805f9-7e8b-44fe-91a7-a84a3b83eb50
    nicName: net1
  [2]:
    macAddress: FE:FC:FE:5E:98:71
    model: e1000
    nicID: 67666518-52c0-40d9-aeb4-d0f9a5e33e35
    nicName: net3
  [3]:
    macAddress: FE:FC:FE:A3:B0:D5
    model: e1000
    nicID: e01943c5-fea9-4f5d-ae60-e472e1ab7491
    nicName: net2
```
