---
sidebar_position: 10
---
 
# get
操作概述: 获取虚拟机控制台的配置
 
命令参数: 
```bash
-v|--vm-ids=array   必要参数，虚拟机id列表，例如：--vm-ids.1 7369491980128 --vm-ids.2 7291549938786
--vm-ids.N=string   vm-ids参数中的每个元素，示例：7291549938786
```
 
使用示例:
```bash
acli vm vnc get --vm-ids.1 7369491980128 --vm-ids.2 7291549938786
```
 
结果示例:
```bash
data:
  [0]:
    isEnabled: false
    vmid: 7291549938786
  [1]:
    isEnabled: false
    vmid: 7369491980128
message:
```