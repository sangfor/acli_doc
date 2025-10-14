---
sidebar_position: 10
---
 
# set
操作概述: 更新虚拟机网卡队列数
 
命令参数: 
```bash
-i|--id=string     必要参数，网卡id，示例：4872898137715:net0
-c|--count=integer 必要参数，网卡队列数，示例：1
```
 
使用示例:
```bash
acli vm nic queuecount set -i 1836960663822:net0 -c 1
```
 
结果示例:
```bash
taskID: host-005056b2894b:280998:1760441353:6913569233831
message: null
targetID: 1836960663822:net0
```