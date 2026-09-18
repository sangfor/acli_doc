---
sidebar_position: 1
---

# list

### 操作概述

查询备份池存储列表

### 命令参数

```bash
-b|--backup=integer             是否只显示备份池中的存储。1=只显示备份池，0=只显示非备份池。枚举=[0, 1]
-s|--samba=integer              是否显示共享目录（samba）。1=显示，0=不显示。枚举=[0, 1]
-q|--query=string               存储名称的模糊匹配模式，用于按名称过滤存储（不区分大小写），示例：nfs
-l|--lt256g-not-display=integer 是否不显示小于256G的硬盘。1=不显示，0=显示。默认=1 枚举=[0, 1]
-S|--s3-not-display=integer     是否不显示s3存储。1=不显示，0=显示。默认=0 枚举=[0, 1]
```

### 使用示例

```bash
acli storage backuppool list
acli storage backuppool list --backup 1 --samba 1
```

### 结果示例

```bash
{
  "data": [
    {
      "backup_total": 0,
      "backup_used": 1048576,
      "enable": 0,
      "name": "lv_1788498920",
      "status": 1,
      "storage": "36000c295d99e6f3fa5cbecdd69ab905b_0050568e74c8",
      "type": "local",
      "usable": 1
    },
    {
      "backup_total": 0,
      "backup_used": 4096,
      "enable": 0,
      "name": "虚拟存储卷1",
      "nfstype": "vsnfs",
      "status": 1,
      "storage": "8a83211f_vs_vol_rep3",
      "type": "vsnfs",
      "usable": 1
    },
    {
      "backup_total": 0,
      "backup_used": 1048576,
      "enable": 0,
      "name": "lv_1788505284",
      "status": 1,
      "storage": "36000c29314cd19d551b5fa23ceadd85a_0050568ec35e",
      "type": "local",
      "usable": 1
    },
    {
      "backup_total": 0,
      "backup_used": 1048576,
      "enable": 0,
      "name": "lv_1788505226",
      "status": 1,
      "storage": "36000c29e4768b003a742abc581f351e3_0050568e3fe4",
      "type": "local",
      "usable": 1
    }
  ]
}
```
