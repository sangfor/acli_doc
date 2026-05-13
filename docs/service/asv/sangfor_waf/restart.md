---
sidebar_position: 1
---

# restart

### 操作概述

重启sangfor_waf服务

### 命令参数

无参数

### 使用示例

```bash
acli service asv sangfor_waf restart
```

### 结果示例
```bash
acli service asv sangfor_waf restart

Stoping sangfor_waf: :checking stop status: getcmdpid return 1, get pids: :  OK!.
 Physical cores < 16: 8checking before start: getcmdpid return 1, get pids: :Start (supervisor --lock-file '/var/run/supervisor/sangfor_waf.suplock' --flag-file '*' --flag 011 --prerun 'bash /sf/bin/sangfor_waf_prepare.sh' -w '/sf/waf/local/nginx/sbin/sangfor_waf -e /sf/log/sangfor_waf/sangfor_waf.log -p /sf/waf/local/nginx') OK!.
```
