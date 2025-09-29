---
sidebar_position: 10
---

# netstat
操作概述: 调用系统netstat命令

命令参数:
```bash
无
```

使用示例:
```bash
acli system netstat
```

结果示例:
```bash
# acli system netstat -i
Kernel Interface table
Iface   MTU Met   RX-OK RX-ERR RX-DRP RX-OVR    TX-OK TX-ERR TX-DRP TX-OVR Flg
eth0       1500 0  52942141      0    380 0      11007741      0      0      0 BMPRU
eth0:0     1500 0       - no statistics available -                        BMPRU
eth1       1500 0  56048496      0      0 0            24      0      0      0 BMPRU
eth2       1500 0  40600749      0    105 0            57      0      0      0 BMPRU
eth3       1500 0  40600006      0    105 0            62      0      0      0 BMPRU
eth4       1500 0  56048962      0      0 0            25      0      0      0 BMPRU
eth5       1500 0  43355019      0    372 0       2450923      0      0      0 BMPRU
lo        65536 0  38163916      0      0 0      38163916      0      0      0 LRU
p_eth1     1600 0  56102362      0    105 0          4148      0      0      0 ABMPRU
p_eth4     1600 0  56105612      0    105 0            24      0      0      0 ABMPRU
pcapif1    1500 0         0      0      0 0            23      0      0      0 BMPRU
pcapif2    1500 0         0      0      0 0            23      0      0      0 BMPRU
pcapif3    1500 0         0      0      0 0            23      0      0      0 BMPRU
pcapif4    1500 0         0      0      0 0            23      0      0      0 BMPRU
tunnel     1500 0         0      0      0 0            25      0      0      0 BMPRU
vxlan0     1500 0  41813279      0  74211 0          1027      0      0      0 BMPRU
```