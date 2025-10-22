---
sidebar_position: 10
---

# get
操作概述: 查看流量镜像信息

命令参数:
```bash
-i|--id=string                      必要参数，流量镜像id，例如：3e1be084-e194-417e-a30d-652c3b415143
```

使用示例:
```bash
acli network anet mirror get --id c8e0562c-663d-41d6-be8c-4e6bb2617ae5
```

结果示例:
```bash
flow_mirror:
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