---
sidebar_position: 10
---

# get
操作概述: 获得HCI版本、补丁、架构和集群信息

命令参数:
```bash
无
```

使用示例:
```bash
acli platform info get
```

结果示例:
```bash
[cluster]
ip=10.131.197.5
name=
mask=255.255.240.0
6.8.0_R2
build 2023-11-04 15:20:15
Linux host-005056897c0a 4.18.0-6.8.0_R2 #1 SMP Tue Sep 2 13:17:28 CST 2025 x86_64 GNU/Linux
Cluster Status:

Member Name             ID              Status          IP
host-005056b29527       1454544167      Online          10.131.200.42
host-005056897c0a       1451850762      Online, Local   10.131.203.156

Cluster Stable: Yes
[cluster]
mcastaddr=239.168.50.42
authkey=56b356495eed410696c3a2600d1ac4d8
2025-08-26 13:31:53    update  | [ ] ---> [6.8.0_R2-001 build 2023-11-04 15:20:15]
2025-08-26 19:52:37    patch   | sp-HCI-6.8.0_R2-col-20250826 01-sp-HCI-6.8.0_R2-col-20250826 build 2025-08-26 19:02:57
2025-08-27 19:04:49    patch   | sp-HCI-6.8.0_R2-col-20250827 01-sp-HCI-6.8.0_R2-col-20250827 build 2025-08-27 18:03:59
2025-08-28 17:47:40    patch   | sp-HCI-6.8.0_R2-col-20250828 01-sp-HCI-6.8.0_R2-col-20250828 build 2025-08-28 16:23:40
2025-09-02 17:03:36    patch   | sp-HCI-6.8.0_R2-col-20250902 01-sp-HCI-6.8.0_R2-col-20250902 build 2025-09-02 16:24:30
2025-09-02 18:01:31    patch   | sp-HCI-6.8.0_R2-col-20250902 01-sp-HCI-6.8.0_R2-col-20250902 build 2025-09-02 16:24:30
```