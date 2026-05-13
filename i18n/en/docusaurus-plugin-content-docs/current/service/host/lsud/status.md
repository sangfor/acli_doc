---
sidebar_position: 1
---

# status

### Overview

Check lsud service status

### Command Parameters

No parameters

### Usage Example

```bash
acli service host lsud status
```

### Output Example

```bash
● lsud.service - [sfHCI] hostd
     Loaded: loaded (/etc/systemd/system/lsud.service; enabled; preset: disabled)
     Active: activating (auto-restart) (Result: exit-code) since Thu 2025-11-20 22:08:17 GMT-8; 1s ago
    Process: 4099533 ExecStart=/sf/bin/lsud -f /sf/cfg/lsud/lsud.yaml (code=exited, status=2)
    Process: 4099556 ExecStartPost=/bin/bash -c cgclassify -g cpuset,cpu,cpuacct:/management/strict/low/system $MAINPID || true (code=exited, status=0/SUCCESS)
   Main PID: 4099533 (code=exited, status=2)
```