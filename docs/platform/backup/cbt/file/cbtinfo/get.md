---
sidebar_position: 10
---
 
# get
操作概述: 显示虚拟机目录下所有磁盘的CBT信息
 
命令参数: 
```bash
  -v|--vm-dir=string                  必要参数，指定磁盘目录路径，可从HCI前台，虚拟机详情界面获取，示例：/sf/data/lv_1764129830/disks/08/57/019b4ef9-f7cd-7cdf-bee1-08571ac1ddd1/
  -s|--snap-id=string                 指定快照ID，可选参数，示例：b09981bc-1002-48d0-95c5-efc349cf13f1
```
 
使用示例:
```bash
acli platform backup cbt file cbtinfo get --vm-dir="/sf/data/lv_1764129830/disks/08/57/019b4ef9-f7cd-7cdf-bee1-08571ac1ddd1/" -s=b09981bc-1002-48d0-95c5-efc349cf13f1
acli platform backup cbt file cbtinfo get -v="/sf/data/lv_1764129830/disks/08/57/019b4ef9-f7cd-7cdf-bee1-08571ac1ddd1/"
```
 
结果示例:
```bash
{
    "019b69cf-c958-760c-8e49-83b13ebec9c7.qcow2":   4294967299
}

```