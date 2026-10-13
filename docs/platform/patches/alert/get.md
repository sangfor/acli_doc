---
sidebar_position: 1
---

# get

### 操作概述

查询补丁服务的告警信息

### 命令参数

```bash
无参数
```

### 使用示例

```bash
acli platform patches alert get
```

### 结果示例

```bash
{
  "agent_mode": 2,
  "failed_packs": 0,
  "network_connection": false,
  "not_installed_packs": 0,
  "server_enable": 0,
  "upgrading_packs": 0,
  "warn": {
    "high": {
      "cron": "0 0 0/1 * * ?"
    },
    "level": "",
    "low": {
      "cron": "0 0 0/12 * * ?"
    },
    "middle": {
      "cron": "0 0 0/4 * * ?"
    }
  }
}
```
