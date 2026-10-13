---
sidebar_position: 1
---

# set

### 操作概述

修改虚拟机网卡的自定义 qemu 开机参数（冷编辑，仅支持关机状态下修改）

### 命令参数

```bash
-v|--vm-id=string     必要参数，虚拟机ID，示例：6520699837375
-t|--type=string      必要参数，作用粒度，枚举值：vm（修改虚拟机全部网卡）、nic（仅修改 --nic-id 指定的单个网卡），大小写不敏感，示例：nic。仅支持关机状态下修改
-n|--nic-id=string    可选参数，网卡ID（iface_id），示例：f89a68a0-e44f-494b-9c52-7c47100cfddd。--type nic 时必须指定；--type vm 时忽略
-V|--value=string     必要参数，自定义 qemu 开机参数串（裸逗号分隔），示例：mq=on,vectors=8。整体覆盖：传值则替换，传空串则清空。注意：值以 - 开头时必须用 = 形式传参，值中不能包含高危 Linux 命令字样，否则会被安全控制拦截
```

### 使用示例

```bash
# 修改单个网卡
acli vm advcfg nic-args set -v 6520699837375 -t nic -n f89a68a0-e44f-494b-9c52-7c47100cfddd -V "mq=on,vectors=8"
# 批量修改全部网卡
acli vm advcfg nic-args set -v 6520699837375 -t vm -V "mq=on,vectors=8"
```

### 结果示例

修改单个网卡（`--type nic`）：

```bash
您确定要执行这个操作? (y[es]/n[o]): y
nicID: f89a68a0-e44f-494b-9c52-7c47100cfddd
nicIDs:
  [0]: f89a68a0-e44f-494b-9c52-7c47100cfddd
perNicChanges:
  [0]:
    customArgsAfter: mq=on,vectors=8
    customArgsBefore:
    index: 0
    nicID: f89a68a0-e44f-494b-9c52-7c47100cfddd
    nicName: net0
scope: nic
vmID: 6520699837375
```

批量修改全部网卡（`--type vm`）：

```bash
您确定要执行这个操作? (y[es]/n[o]): y
nicIDs:
  [0]: f89a68a0-e44f-494b-9c52-7c47100cfddd
perNicChanges:
  [0]:
    customArgsAfter: mq=on,vectors=8
    customArgsBefore:
    index: 0
    nicID: f89a68a0-e44f-494b-9c52-7c47100cfddd
    nicName: net0
scope: vm
vmID: 6520699837375
```