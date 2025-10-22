---
sidebar_position: 10
---

# set
操作概述: 调整nat表项限制

命令参数:
```bash
-m|--max-size=integer               必要参数，nat表项配置规格，65536（最小），131072（最大）

```

使用示例:
```bash
acli network anet config nat set -m 65536
```

结果示例:
```bash
命令执行成功！
```