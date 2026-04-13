---
sidebar_position: 1
---

# clean

### 操作概述

清理磁盘残留信息

### 命令参数

```bash
-p|--path=string                   必要参数，块设备路径，示例：/dev/sdc
```

### 使用示例

```bash
acli storage asan disk residual clean -p /dev/sdc
```

### 结果示例

```bash
[INFO] =====目标设备: /dev/sdd=====
[INFO] 目标设备: /dev/sdd (类型: disk)
[INFO] 正在执行安全状态检查...
[INFO] 安全检查通过：设备及子设备当前未被系统挂载或用作 Swap
[INFO] 正在检查并清理 LVM 结构...
[WARN] 检测到残留的 LVM VG 'vg_test'。尝试去激活并移除...
[INFO] 已成功通过标准路径移除 VG 'vg_test'
[INFO] 正在检查并清理底层的 LVM PV 标签...
[WARN] 检测到孤立的 LVM PV 残留，正在执行 pvremove...
[INFO] 已清理 /dev/sdd1 上的 LVM PV 标签
[INFO] 开始分析并清理底层残留签名...
[INFO] 正在执行 wipefs -a 精准清除所有已知签名...
[INFO] /dev/sdd 签名已清除
[INFO] /dev/sdd1 签名已清除
[INFO] 正在对头部和尾部进行物理清零
[INFO] 头部和尾部物理清零完成, TARGET_DEV:/dev/sdd
[INFO] 正在通知内核重新读取分区表...
[INFO] 内核分区表已刷新（原有分区节点应该已消失）
[INFO] =====目标设备: /dev/sdd 清理完成=====

```
