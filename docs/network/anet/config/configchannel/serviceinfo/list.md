---
sidebar_position: 10
---

# list
操作概述: 获取网络配置通道各服务当前健康状态

命令参数:  
```bash
无
```

使用示例:
```bash
acli network anet config configchannel serviceinfo list
```

结果示例:
```bash
    host             |service           |status
    -----------------|------------------|-------
1   host-005056b223bc|vn-lcp            |Healthy
2   null             |kafka             |Healthy
3   host-005056b2d4e1|vn-lcp            |Healthy
4   host-005056b2d4f1|vn-lcp            |Healthy
5   null             |vn-ccp            |Healthy
6   null             |vn-manager-service|Healthy
```

