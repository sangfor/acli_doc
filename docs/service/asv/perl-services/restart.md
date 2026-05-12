---
sidebar_position: 1
---

# restart

### 操作概述

重启基础的perl相关的服务

### 命令参数

无参数

### 使用示例

```bash
acli service asv perl-services restart
```

### 结果示例
```bash
acli service asv perl-services restart

You can add more services as '/sf/debug/sfd-restart-perl-services.sh service1 service2' to restart them.
Restarting the basic perl services.
restarting vtpperlproxy
restarting vtpdaemon
restarting apache2
```
