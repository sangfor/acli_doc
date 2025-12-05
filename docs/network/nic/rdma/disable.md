---
sidebar_position: 10
---

# disable
操作概述: 关闭指定厂商的指定ib网卡设备的rdma功能

命令参数:
```bash
-v|--vendor=string        必要参数，厂商id，示例：0x15ad
-i|--ib-dev=string        必要参数，ib网卡设备名称，示例：hinic0      
```

使用示例:
```bash
acli network nic rdma disable --vendor 0x15ad --ib-dev hinic0
```

结果示例:
```bash
***************** Current Info *******************
[Current   ] Cfg template index :  0
***************** Next Reset Cfg *****************
[Next Reset] Max support index  :  3
[Next Reset] Cfg template index :  2
[Next Reset] Firmware support cfg template name:
             Template[ 0]: NIC_2X25G
             Template[ 1]: NIC_2X25G_3PF_120VF
             Template[ 2]: ROCE_2X25G
             Template[ 3]: NIC_2X25G_4PF
```