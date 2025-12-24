---
sidebar_position: 10
---
 
# disable
操作概述: 禁用虚拟机控制台的访问权限
 
命令参数: 
```bash
-v|--vm-ids=array   必要参数，虚拟机id列表，例如：--vm-ids.1 7369491980128 --vm-ids.2 7291549938786
--vm-ids.N=string   vm-ids参数中的每个元素，示例：7291549938786
```
 
使用示例:
```bash
acli vm vnc disable --vm-ids.1 7369491980128 --vm-ids.2 7291549938786
```
 
结果示例:
```bash
# 成功
code: 0
message:
# 失败
code: 500
message: "更新VNC配置失败。"
```