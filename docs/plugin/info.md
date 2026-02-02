---
sidebar_position: 40
---

# info
操作概述: 查询指定插件的详细信息

命令参数:
```bash
--name, -n  string  必要参数，插件名称，查询多个请使用英文逗号连接，示例：plugin_1,plugin_2
```

使用示例:
```bash
acli plugin info --name plugin_name
```

结果示例:
```bash
Name       Version  Status    Title              VendorName
plugin_xxx  1.0.0    enabled   插件标题           深信服