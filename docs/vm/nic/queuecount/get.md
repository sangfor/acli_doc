---
sidebar_position: 10
---
 
# get
操作概述: 获取虚拟机网卡队列数
 
命令参数: 
```bash
-i|--id=string 必要参数，网卡id，示例：4872898137715:net0
 
使用示例:
```bash
acli vm nic queuecount get --id 1836960663822:net0
```
 
结果示例:
```bash
numQueues: 1
```