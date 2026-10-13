---
sidebar_position: 1
---

# set

### 操作概述

修改虚拟机CPU的自定义 qemu 开机参数（冷编辑，仅支持关机状态下修改；ARM 平台不支持，会返回错误）

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机ID，示例：6520699837375
-V|--value=string    必要参数，CPU 自定义 qemu 开机参数串（裸逗号分隔），示例：hv_vendor_id=CustomOEM。整体覆盖：传值则替换，传空串则清空
```

### 使用示例

```bash
acli vm advcfg cpu-args set -v 6520699837375 -V hv_vendor_id=CustomOEM
```

### 结果示例

```bash
您确定要执行这个操作? (y[es]/n[o]): y
customArgsAfter: hv_vendor_id=CustomOEM
customArgsBefore:
vmID: 6520699837375
```

虚机处于运行状态时会被拒绝：

```bash
错误：虚拟机正在运行，修改自定义 qemu 参数需先关机！
```