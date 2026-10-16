---
sidebar_position: 3
---

# restore

### 操作概述

恢复主机 nohz_full 启动参数

### 命令参数

```bash
-h|--hostname=string    主机节点名，格式如 host-0cc47a6bd88e，不传时默认本机
-g|--grub-root=string   grub 目录路径，必须以 /boot/grub 结尾；aSV 容器化部署默认 /boot/boot/grub，物理机直装场景需显式传 /boot/grub
```

### 使用示例

```bash
acli platform node nohz-full restore
acli platform node nohz-full restore -h host-0cc47a6bd88e
acli platform node nohz-full restore -h host-0cc47a6bd88e -g /boot/grub
```

### 结果示例

```bash
success: 1
action: restore
grub_root: /boot/boot/grub
```
