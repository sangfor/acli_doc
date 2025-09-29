---
sidebar_position: 10
---

# iptables
操作概述: iptables命令用于配置Linux内核的防火墙规则。

命令参数:
```bash
无
```

使用示例:
```bash
acli system iptables
```

结果示例:
```bash
# acli system iptables -L -n -v
Chain INPUT (policy DROP 128 packets, 5128 bytes)
 pkts bytes target     prot opt in     out     source               destination 
3948K  703M TMP_RULES  all  --  *      *       0.0.0.0/0            0.0.0.0/0   
3947K  703M VS_TMP_RULES  all  --  *      *       0.0.0.0/0            0.0.0.0/0
```