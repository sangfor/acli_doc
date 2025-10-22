---
sidebar_position: 10
---

# set
操作概述: 更新聚合口

命令参数:  
```bash
-h|--hostname=string                主机id，例如：host-005056b2a30a
-b|--bond-name=string               必要参数，聚合口名称，例如：channel1
-m|--members=string                 成员口名称，多个成员口使用逗号分隔，例如：eth2,eth3
-d|--mode=string                    聚合口模式: active-backup(静态聚合，主备模式mode:1), layer2(静态聚合，使用mac地址负载mode: 2), layer23(静态聚合，使用ip地址负载mode: 2), balance-rr(静态聚合：根据网口轮询mode:0), layer34(静态聚合，四层信息进行负载mode:2), lacp-layer2(LACP模式，根据MAC地址进行负载mode:4)， lacp-layer23(LACP模式，根据ip地址进行负载mode:4)， lacp-layer34(LACP模式，根据四层信息进行负载mode:4)

```

使用示例:
```bash
acli network bond set --hostname host-005056b2ec8d --bond-name channel1 --members eth2,eth3 --mode layer23
```

结果示例:
```bash
task_id: UPID:host-005056b2ec8d:00009AFB:1ADD4A0:6875BA28:编辑网口:16:admin@vtp:
```
