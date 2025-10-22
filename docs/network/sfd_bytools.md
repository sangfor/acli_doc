---
sidebar_position: 10
---

# sfd_bytools
操作概述: 数据面sfd_byTools.sh脚本

命令参数:
```bash
无
```

使用示例:
```bash
acli network sfd_bytools
```

结果示例:
```bash
usage: /sf/sdn/bin/sfd_byTools.sh option
--dvs [dvsname],                                     show dvswitches
--vr [vrname],                                       show vrouters
--vlink,                                             show all vlinks
--vlan [dvsname [vslink]],                           show dvswitch's vslink vlan
--vslink [dvsname [vslink]],                         show dvswitch's vlink information
--vrlink [vrname [vrlink]],                          show vrouter's vlink information
--fdb [devname],                                     show net device forwording database
--arp,                                               show system arp table
--pcap vlink/ethx pcapif[1-4] [timeout <1-65535>],   pcap vlink's/ethx's package, default timeout 10 min
--show-pcap-all,                                     show all pcapifx information
--no-pcap [pcapif]                                   no pcap vlink, pcapif should be pcapif[1-4]
--help,                                              show help information
```
