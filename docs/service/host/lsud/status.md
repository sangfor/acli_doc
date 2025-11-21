---
sidebar_position: 10
---

# status
操作概述: 查询lsud服务状态

命令参数:
```bash
无
```

使用示例:
```bash
acli service host lsud status
```

结果示例:
```bash
● lsud.service - [sfHCI] hostd
     Loaded: loaded (/etc/systemd/system/lsud.service; enabled; preset: disabled)
     Active: activating (auto-restart) (Result: exit-code) since Thu 2025-11-20 22:08:17 GMT-8; 1s ago
    Process: 4099533 ExecStart=/sf/bin/lsud -f /sf/cfg/lsud/lsud.yaml (code=exited, status=2)
    Process: 4099556 ExecStartPost=/bin/bash -c cgclassify -g cpuset,cpu,cpuacct:/management/strict/low/system $MAINPID || true (code=exited, status=0/SUCCESS)
   Main PID: 4099533 (code=exited, status=2)
```