---
sidebar_position: 1
---

# info                                                                                                                         
                                                                                                                                                     
### 操作概述                                                                                                                                       
                                                                                                                                                 
获取指定插件信息                                                                           
                                                                                                                                                 
### 命令参数                                                                                                                                       
                                                                                                                                                 
```bash                                                                                                                                            
-n|--name=string    必要参数，插件名称，查询多个请使用英文逗号连接，示例：plugin_1,plugin_2                                                        
```

### 使用示例                                                                                                                                           
                                                                                                                                                 
```bash
acli plugin info -n plugin_1                                                                                                                       
acli plugin info --name=plugin_1,plugin_2                                                                                                          
```

### 结果示例                                                                                                                                           

```bash                                                                                                                                                 
acli plugin info -n asan_ops,vm_start
[0]:
  ACliVersion: >=1.0.0
  Arch: x86
  ChangeLog:
  Dependencies:
  Description: 虚拟存储异常场景排障工具
  HCIVersion: >=6.12.0
  Name: asan_ops
  Source: 官方包
  Status: 开启
  Title: 虚拟存储异常场景排障工具
  VendorName:
  Version: 1.0.0
[1]:
  ACliVersion: >=1.0.0
  Arch: x86
  ChangeLog:
  Dependencies:
  Description: 虚拟机开关机场景排障
  HCIVersion: >=6.12.0
  Name: vm_start
  Source: 官方包
  Status: 开启
  Title: 虚拟机开关机场景排障
  VendorName:
  Version: 1.0.0
                                                                                                       
```