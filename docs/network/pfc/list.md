---
sidebar_position: 1
---

# list

### 操作概述

查询优先级流控(PFC)配置列表

### 命令参数

```bash
-d|--domain-id=string    可选，网络平面ID（UUID），用于按网络平面过滤；不传则返回全部流控配置
```

### 使用示例

```bash
acli network pfc list
acli network pfc list -d 960d7a90-aad3-4f5c-b57f-5e3f61098ae2
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
[1]:
  domainId:
    [0]: ff348d34-e4ed-40bb-a0ab-0ba24523eda7
  dscpTag: 46
  enable: true
  id: 61d20b69-894e-419e-9577-4e839e9195aa
  trust: dscp
```
