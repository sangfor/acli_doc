---
sidebar_position: 10
---

# check
操作概述: 检查虚拟机vlink状态

命令参数:
```bash
-s|--service=string 检查的类型，枚举值：vm(虚拟机)，cluster(当前集群所有虚拟机)， host(当前主机)， nk(北向kafka)， sk(南向kafka)， vt(平台)， mp(管理面)， ccp(中心控制器)， redis(redis缓存)， lcp(本地控制器)， dp(数据面)
-v|--vm-id=string 虚拟机id，例如：7332207472995
-h|--hostname=string 主机id，例如：host-005056b2ec8d
```

使用示例:
```bash
acli network vlink check --service vm --vm-id 1517895970957
```

结果示例:
```bash
=== 服务查询结果 ===
Service     VMPort                                Location           Peer
VM          1517895970957                         host-005056b2ec8d  -
MP          8ac58d3b-5f79-40d6-af36-a5fc03d90d21  host-005056b2ec8d  80a6cc4a-4fc9-438b-8757-d97e4671990c
NorthKafka  未检测到                          未检测到       未检测到
CCP         8ac58d3b-5f79-40d6-af36-a5fc03d90d21  host-005056b2ec8d  80a6cc4a-4fc9-438b-8757-d97e4671990c
SouthKafka  未检测到                          未检测到       未检测到
Redis       8ac58d3b-5f79-40d6-af36-a5fc03d90d21  host-005056b2ec8d  80a6cc4a-4fc9-438b-8757-d97e4671990c
LCP         8ac58d3b-5f79-40d6-af36-a5fc03d90d21  host-005056b2ec8d  80a6cc4a-4fc9-438b-8757-d97e4671990c
DP          8ac58d3b-5f79-40d6-af36-a5fc03d90d21  host-005056b2ec8d  80a6cc4a-4fc9-438b-8757-d97e4671990c

=== 注意事项 ===
1、执行所有处置之前，请先使用工具收集日志。
2、Kafka和CCP的信息源均为服务储存的增量消息日志，非全量配置信息，如果无法查到相关配置的准确信息，则输出为"未检测到"。
3、除Kafka和CCP服务外其他服务信息源均为全量配置信息，如果无法查到相关配置信息，输出为"不存在"。
4、Location以VM提供信息为基准，其他均以MP提供的配置信息为基准。
5、此工具无法保证检测过程中各层服务配置的一致性，在使用工具的过程中尽量不要进行网络配置更新，否则可能产生误判，可以尝试多次执行检查进一步确认问题。
```
