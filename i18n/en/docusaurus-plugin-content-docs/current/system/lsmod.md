---
sidebar_position: 1
---

# lsmod

### Overview

View kernel modules using the lsmod command

### Command Parameters

No parameters
### Usage Example

```bash
acli system lsmod
```

### Output Example

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