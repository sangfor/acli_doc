---
sidebar_position: 10
---

# status
操作概述: 查询hostd服务状态

命令参数:
```bash
无
```

使用示例:
```bash
acli service host hostd status
```

结果示例:
```bash
● hostd.service - [sfHCI] hostd
     Loaded: loaded (/etc/systemd/system/hostd.service; enabled; preset: disabled)
     Active: active (running) since Thu 2025-11-20 22:02:41 GMT-8; 2min 26s ago
    Process: 4056545 ExecStartPost=/bin/bash -c cgclassify -g cpuset,cpu,cpuacct:/management/strict/high/system $MAINPID || true (code=exited, status=0/SUCCESS)
   Main PID: 4056536 (hostd)
      Tasks: 15 (limit: 131804)
     Memory: 26.6M (max: 200.0M available: 173.3M)
     CGroup: /system.slice/hostd.service
             └─4056536 /sf/bin/hostd -f /sf/cfg/hostd/hostd.yaml
```