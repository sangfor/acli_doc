---
sidebar_position: 10
---

# list
操作概述: 查看mac表容量

命令参数:
```bash
无
```

使用示例:
```bash
acli network anet mirror list
```

结果示例:
```bash
total: 1
flow_mirrors:
    direction: All
    enable: 0
    description:
    samplingRate: 100
    dstVlan: null
    dstIfaceId: 4d3a0d8c-2f05-4592-adc8-8a9eb5efd897
    tenantId: 707e9d9dac814227b90941362efb6616
    srcIfaceIds: 8ac58d3b-5f79-40d6-af36-a5fc03d90d21
    id: c8e0562c-663d-41d6-be8c-4e6bb2617ae5
    name: qcl
```