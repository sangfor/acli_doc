---
sidebar_position: 5
---

# core 命名空间
网络数据面转发核相关操作

## get命令
操作概述: 查看数据面转发核

命令参数:  
```bash
无
```

使用示例:
```bash
acli platform service dp core get
```

结果示例:
```bash
   highPerformance: false
   forwardCores: 2
```

## set命令
操作概述: 设置数据面转发核

命令参数:  
```bash
-h|--high-performance=integer 转发核是否独占，0（关闭），1（开启）
-c|--forward-cores=integer 转发核数量，例如：8
```

使用示例:
```bash
acli platform service dp core set --high-performance 1 --forward-cores 2
```

结果示例:
```bash
   highPerformance: true
   forwardCores: 2
```
