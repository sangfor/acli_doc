---
sidebar_position: 10
---

# get
操作概述: 获取平台mysql服务的配置

命令参数:
```bash
无
```

使用示例:
```bash
acli platform mysql config get
```

结果示例:
```bash
# CHKVER:3# ***DO NOT EDIT FIRST LINE***
[mysqld]
server-id                    = 1
max_connections              = 750
rpl_semi_sync_slave_enabled  = ON
rpl_semi_sync_master_enabled = ON
super_read_only              = 0
read_only                    = 0
report_host                  = host-005056893c9d
```