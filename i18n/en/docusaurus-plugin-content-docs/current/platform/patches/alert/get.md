---
sidebar_position: 1
---

# get

### Overview

Get patch service alert info

### Command Parameters

```bash
No parameters
```

### Usage Example

```bash
acli platform patches alert get
```

### Output Example

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
