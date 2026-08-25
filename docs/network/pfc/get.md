---
sidebar_position: 2
---

# get

### 操作概述

查询单条优先级流控(PFC)配置（按 domainId 过滤后取首条；后端无 get-by-id 端点）

### 命令参数

```bash
-d|--domain-id=string    必要参数，网络平面ID（UUID），用于按网络平面过滤查询流控配置，示例：960d7a90-aad3-4f5c-b57f-5e3f61098ae2
```

### 使用示例

```bash
acli network pfc get -d 960d7a90-aad3-4f5c-b57f-5e3f61098ae2
```

### 结果示例

```bash
[0]:
  cnpDscp: 48
  cnpPrio: 3
  domainId:
    [0]: 960d7a90-aad3-4f5c-b57f-5e3f61098ae2
  dscpTag: 26
  enable: true
  id: 215613f8-4ee3-4d56-a602-d05fe9cd484c
  trust: dscp
```
