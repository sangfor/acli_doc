---
sidebar_position: 10
---

# get
操作概述: 查看网口队列数

命令参数:  
```bash
-n|--nic-name=string        必要参数，网口名称，例如：eth1, channel1
```

使用示例:
```bash
acli network nic queue get --nic-name eth4
```

结果示例:
```bash
eth4
   ring_count:
      current: 0
      max: 0
      initial: 0
   name: eth4
   id: eth4
```

