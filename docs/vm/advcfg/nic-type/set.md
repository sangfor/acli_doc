---
sidebar_position: 1
---

# set

### 操作概述

设置虚拟机网卡类型（冷编辑，VM 必须处于关机态）。该命令将 VM 全部网卡统一改为目标型号，不改单张；执行前会触发二次确认；修改在 VM 下次开机时生效于 qemu 层。

约束：
- VM 必须关机，开机态拒绝修改（HTTP 500）。
- 仅支持 `virtio` / `e1000` 两种型号，大小写不敏感。
- Windows 未装 vmtools 时禁止 e1000→virtio（virtio 驱动依赖 vmtools），反方向与 Linux 双向均不受限。

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机ID，必须是纯数字组合，示例：4133790374747
-m|--model=string    必要参数，目标网卡型号，枚举值，virtio：高性能半虚拟化网卡驱动，需客户机安装 vmtools 后才可使用；e1000：Intel 82540EM 模拟网卡，兼容性最佳无需 vmtools；大小写不敏感，示例：virtio
```

### 使用示例

```bash
acli vm advcfg nic-type set --vm-id 4133790374747 --model virtio
```

### 结果示例

```bash
您确定要执行这个操作? (y[es]/n[o]): y
newModel: virtio
nics:
  [0]:
    mac: FE:FC:FE:0D:5D:88
    newModel: virtio
    nicID: 34a89548-2923-4a87-93ab-ee71846fb6ba
    nicName: net0
    oldModel: e1000
  [1]:
    mac: FE:FC:FE:D3:B0:44
    newModel: virtio
    nicID: a05805f9-7e8b-44fe-91a7-a84a3b83eb50
    nicName: net1
    oldModel: e1000
  [2]:
    mac: FE:FC:FE:5E:98:71
    newModel: virtio
    nicID: 67666518-52c0-40d9-aeb4-d0f9a5e33e35
    nicName: net3
    oldModel: e1000
  [3]:
    mac: FE:FC:FE:A3:B0:D5
    newModel: virtio
    nicID: e01943c5-fea9-4f5d-ae60-e472e1ab7491
    nicName: net2
    oldModel: e1000
oldModel: e1000
vmID: 4133790374747
```
