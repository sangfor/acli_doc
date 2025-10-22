---
sidebar_position: 10
---

# get
操作概述: 查看当前网口环形缓冲区参数

命令参数:
```bash
-n|--nic-name=string        必要参数，网口名称，例如：eth1, channel1
```

使用示例:
```bash
acli network nic ring get --nic-name eth4
```

结果示例:
```bash
eth4
   ring_buffer:
      current:
         rx: 1024
         tx: 512
      max:
         rx: 4096
         tx: 4096
      initial:
         rx: 1024
         tx: 512
   name: eth4
   id: eth4
```