---
sidebar_position: 5
---

# mac 命名空间
数据面mac配置相关操作

## get命令
操作概述: 查看mac表项限制

命令参数:  
```bash
无
```

使用示例:
```bash
acli platform service dp mac get
```

结果示例:
```bash
mac_table_learn_limit: 51000
```

## set命令
操作概述: 调整mac表项限制

命令参数:  
```bash
-l|--learn-limit=integer mac表容量规格，51000（最小），262144（最大）
```

使用示例:
```bash
acli platform service dp mac set --learn-limit 52000
```

结果示例:
```bash
命令执行成功!
```
