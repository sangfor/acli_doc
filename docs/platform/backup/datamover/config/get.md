---
sidebar_position: 1
---

# get

### 操作概述

查询datamover配置文件内容

### 命令参数

```bash
-f|--filename=string    必要参数，指定要查询的配置文件名称，枚举值为：'setting', 'default', 'backup-task-config-template', 'writespeed-task-config-template'
```

### 使用示例

```bash
acli platform backup datamover config get --filename=setting
acli platform backup datamover config get -f=default
```

### 结果示例

```bash
{"suspend_timeout": 600, "progress_interval_secs": 10, "terminate_wait_secs": 30, "plugin_dir": "", "backup_task_template_path": "/usr/share/perl5/VTP/Vm/Backup/Datamover/backup_task_config_template.json", "cancel_wait_secs": 30, "debug_on": 0, "cancel_interval_secs": 30, "datamover_bin": "/sf/bin/datamover", "writespeed_task_template_path": "/usr/share/perl5/VTP/Vm/Backup/Datamover/writespeed_task_config_template.json", "progress_retry_max_cnt": 18, "http_timeout": 600}

```
