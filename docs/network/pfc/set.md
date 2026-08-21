---
sidebar_position: 4
---

# set

### 操作概述

更新优先级流控(PFC)配置（异步任务，返回 taskId）

### 命令参数

```bash
-i|--flowcontrol-id=string    必要参数，流控配置ID（UUID），用于定位待更新的流控配置
-d|--data=object              必要参数，更新流控配置参数（JSON 对象）
                                字段：
                                  enable      bool    必填，是否启用
                                  trust       string  必填，信任模式，取值：pcp / dscp（小写）
                                  pcpTag      int     选填，trust=pcp 时必填，取值 0-7
                                  dscpTag     int     选填，trust=dscp 时必填，取值 0-63
                                  cnpPrio     int     选填，RoCE 场景，取值 0-7
                                  cnpDscp     int     选填，RoCE 场景，取值 0-63
                                示例：{"enable":true,"trust":"dscp","dscpTag":46}
```

### 使用示例

```bash
# 先 list 拿到 id
acli network pfc list -d 960d7a90-aad3-4f5c-b57f-5e3f61098ae2

# 更新（关闭 enable，改 dscpTag）
acli network pfc set -i 215613f8-4ee3-4d56-a602-d05fe9cd484c -d '{"enable":false,"trust":"dscp","dscpTag":30}'

# 更新 cnp 字段
acli network pfc set -i 215613f8-4ee3-4d56-a602-d05fe9cd484c -d '{"enable":true,"trust":"dscp","dscpTag":30,"cnpPrio":3,"cnpDscp":48}'
```

### 结果示例

```bash
taskId: host-0050568ecad9:1703505460:1
```
