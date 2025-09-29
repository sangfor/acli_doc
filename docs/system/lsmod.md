---
sidebar_position: 10
---

# lsmod
操作概述: 执行lsmod工具进行系统检查

命令参数:
```bash
无
```

使用示例:
```bash
acli system lsmod
```

结果示例:
```bash
Module                  Size  Used by
nfnetlink_log          20480  0
nfnetlink              16384  1 nfnetlink_log
nfsv3                  53248  1
xt_comment             16384  1
rpcsec_gss_krb5        36864  0
nfsv4                 696320  2
dns_resolver           16384  1 nfsv4
iptable_nat            16384  1
nf_nat_ipv4            16384  1 iptable_nat
nf_nat                 36864  1 nf_nat_ipv4
ipt_REJECT             16384  1
nf_reject_ipv4         16384  1 ipt_REJECT
...
```