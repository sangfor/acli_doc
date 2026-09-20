---
sidebar_position: 1
---

# get

### 操作概述

查询 syslog 转发配置

### 命令参数

```bash
无参数
```

### 使用示例

```bash
acli platform syslog config get
```

### 结果示例

```bash
{
  "kernlog_enabled": "0",
  "lang": "zh_CN",
  "oplog_enabled": "0",
  "protocol": "tcp",
  "server_name": "",
  "server_port": "",
  "syslog_enabled": "0"
}
```
