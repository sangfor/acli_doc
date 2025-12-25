---
sidebar_position: 10
---
 
# set
操作概述: 设置区域快照的运行时参数配置
 
命令参数: 
```bash
-v|--vm-id=string                   必要参数，指定虚拟机ID，用于标识要配置的虚拟机，必选参数，示例：7441066936147
-i|--iolog=integer                  是否打印区域快照相关的每个IO的日志，枚举值：0（不打印），1（打印），可选参数，默认值为0
-p|--holeperf=integer               区域快照导出有效数据区时，是否跳过空洞。枚举值：0（不跳过空洞），1（跳过空洞），可选参数，默认值为1
-c|--cowperf=integer                备份读区域快照时，是否启用COW高性能模式。枚举值：0（不启用），1（启用且为direct方式），2（启用且为缓存限制方式），可选参数，默认值为2
-s|--cowcachesize=integer           当cowperf为2（启用且为缓存限制方式）时，通过cowcachesize指定整个虚拟机的COW缓存上限，单位为MB。有效范围：32-1024，可选参数，默认值为256
-m|--cowmerge=integer               区域快照COW合并块数量，每块对应16K。有效范围：1-64，可选参数，默认值为64
-r|--ioretry=integer                区域快照COW写的重试次数。有效范围：0-128，可选参数，默认值为3
-R|--readspeed=integer              读虚拟机区域快照的带宽上限，单位为KB/S。有效范围：1-3072000，可选参数，默认值为81920
-l|--l2cachesize=integer            每个区域快照镜像的L2元数据缓存上限，单位为MB。有效范围：32-1024，可选参数，默认值为256
```
 
使用示例:
```bash
acli platform backup region config set --vm-id=7188533957477 -i 0 --holeperf=1
```
 
结果示例:
```bash
本命令无输出，修改成功后，在/sf/log/today/sfvt_qemu_{vmid}.log中输出
```