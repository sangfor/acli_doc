---
sidebar_position: 1
---

# check

### 操作概述

检测网卡一致性，对比 Qemu、VN、CFS、DB 的 MAC 地址和接口 ID

### 命令参数

```bash
-v|--vm-id=string    必要参数，虚拟机ID，示例：614182240912
```

### 使用示例

```bash
# 检测网卡一致性
acli vm nic consistency check -v 614182240912
```

### 结果示例

```bash
{"VMID":"614182240912","NICs":[{"NICIndex":0,"QemuMAC":"FE:FC:FE:DB:A3:2C","VnMAC":"FE:FC:FE:DB:A3:4C","CfsMAC":"FE:FC:FE:DB:A3:4C","CfsInterfaceID":"800b6b64-0b5d-4552-8372-b27ee991f746","VnInterfaceID":"800b6b64-0b5d-4552-8372-b27ee991f746","DBInterfaceID":"800b6b64-0b5d-4552-8372-b27ee991f746","MacConsistent":false,"IDConsistent":true,"Status":"inconsistent"}],"CheckTime":"2026-05-26T11:17:02+08:00"}
```
