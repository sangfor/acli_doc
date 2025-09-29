---
sidebar_position: 5
---

# nat 命名空间
数据面nat配置相关操作

## get命令
操作概述: 查看nat表项限制

命令参数:  
```bash
无
```

使用示例:
```bash
acli platform service dp nat get
```

结果示例:
```bash
cone_nat_hash_max_size: 131072
```

## set命令
操作概述: 调整nat表项限制

命令参数:  
```bash
-m|--max-size=integer nat表项配置规格，65536（最小），131072（最大）
```

使用示例:
```bash
acli platform service dp nat set --max-size 131073
```

结果示例:
```bash
命令执行成功!
```
