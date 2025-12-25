---
sidebar_position: 10
---
 
# set
操作概述: 开启或关闭datamover性能瓶颈探测
 
命令参数: 
```bash
-v|--vm-id=string                   必要参数，指定datamover对应的虚拟机，示例：7441066936147
-i|--host-id=string                 必要参数，用于指出datamover服务运行的主机节点，示例：host-9cc2c4105d08
-l|--level=string                   必要参数，用于指定开启或关闭datamover的性能瓶颈探测，枚举值为：'OFF'（关闭探测）、'FULL'（全量模式开启探测）、'FAST'（快速模式开启探测）
```
 
使用示例:
```bash
acli platform backup datamover performancedetect set --vm-id=7188533957477 -i=host-9cc2c4105d08 -l=FULL
```
 
结果示例:
```bash
正确案例：
OK
错误案例：
错误：请求失败： 无法找到datamover进程的配置文件路径
```