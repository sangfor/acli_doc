---
sidebar_position: 1
---

# set

### 操作概述

修改虚拟机整机的自定义 qemu 开机参数（冷编辑，仅支持关机状态下修改）

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机ID，示例：6520699837375
-V|--value=string    必要参数，整机自定义 qemu 开机参数串（主板/BIOS args），示例：-no-hpet -nodefaults。整体覆盖：传值则替换，传空串则清空。注意：值以 - 开头时必须用 = 形式传参（如 -V="-no-hpet -nodefaults"），否则会被误判为选项；值中不能包含高危 Linux 命令字样（如 reboot），否则会被安全控制拦截
```

### 使用示例

```bash
acli vm advcfg machine-args set -v 6520699837375 -V="-no-hpet -nodefaults"
```

### 结果示例

```bash
您确定要执行这个操作? (y[es]/n[o]): y
argsAfter: -no-hpet -nodefaults
argsBefore:
vmID: 6520699837375
```

虚机处于运行状态时会被拒绝：

```bash
错误：虚拟机正在运行，修改自定义 qemu 参数需先关机！
```

值含有高危命令字样时会被拦截：

```bash
错误：输入字符串中包含高危 Linux 命令：reboot，操作被拒绝。
```