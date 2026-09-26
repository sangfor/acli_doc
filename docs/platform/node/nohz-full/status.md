---
sidebar_position: 1
---

# status

### 操作概述

查询主机 nohz_full 启动参数状态

### 命令参数

```bash
-h|--hostname=string    主机节点名，格式如 host-0cc47a6bd88e，不传时默认本机
-g|--grub-root=string   grub 目录路径，必须以 /boot/grub 结尾；aSV 容器化部署默认 /boot/boot/grub，物理机直装场景需显式传 /boot/grub
```

### 使用示例

```bash
acli platform node nohz-full status
acli platform node nohz-full status -h host-0cc47a6bd88e
acli platform node nohz-full status -h host-0cc47a6bd88e -g /boot/grub
```

### 结果示例

```bash
grub_root: /boot/boot/grub
files:
  - name: grub.cfg
    exists: true
    has_nohz_full: true
    has_rollback: false
  - name: grub.cfg.kdump
    exists: true
    has_nohz_full: true
    has_rollback: false
```
