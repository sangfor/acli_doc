---
sidebar_position: 1
---

# get

### Overview

get datamover config file

### Command Parameters
```bash
-f|--filename=string    Required parameter, Specify the config file name to get, The enumerated values are: 'setting', 'default', 'backup-task-config-template', 'writespeed-task-config-template', Enum values: setting,backup-task-config-template,writespeed-task-config-template,default
```

### Usage Example

```bash
acli platform backup datamover config get --filename=setting
acli platform backup datamover config get -f=default
```

### Output Example

```bash
{"suspend_timeout": 600, "progress_interval_secs": 10, "terminate_wait_secs": 30, "plugin_dir": "", "backup_task_template_path": "/usr/share/perl5/VTP/Vm/Backup/Datamover/backup_task_config_template.json", "cancel_wait_secs": 30, "debug_on": 0, "cancel_interval_secs": 30, "datamover_bin": "/sf/bin/datamover", "writespeed_task_template_path": "/usr/share/perl5/VTP/Vm/Backup/Datamover/writespeed_task_config_template.json", "progress_retry_max_cnt": 18, "http_timeout": 600}

```