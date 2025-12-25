---
sidebar_position: 10
---
 
# verify
操作概述: 验证CBT文件的完整性和一致性
 
命令参数: 
```bash
-f|--filename=string 必要参数，指定磁盘文件的绝对路径，用于验证该文件的CBT功能是否正常。示例：/sf/xxx/vm-disk-1.qcow2
```
 
使用示例:
```bash
acli platform backup cbt file verify -f="/disks/83/b1/019b69cf-c958-760c-8e49-83b13ebec9c7/vm-disk-1.qcow2"
```
 
结果示例:
```bash
正确案例：
0
错误案例：输出非0时，说明cbt状态异常
```