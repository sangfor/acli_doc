---
sidebar_position: 3
---

# create

### 操作概述

创建优先级流控(PFC)配置（异步任务，返回 taskId）

### 命令参数

```bash
-d|--data=object    必要参数，创建流控配置参数（JSON 对象）
                    字段：
                      domainId    string  必填，网络平面ID（UUID）
                      enable      bool    必填，是否启用
                      trust       string  必填，信任模式，取值：pcp / dscp（小写）
                      pcpTag      int     选填，trust=pcp 时必填，取值 0-7
                      dscpTag     int     选填，trust=dscp 时必填，取值 0-63
                      cnpPrio     int     选填，RoCE 场景，取值 0-7
                      cnpDscp     int     选填，RoCE 场景，取值 0-63
                    示例：{"domainId":"960d7a90-aad3-4f5c-b57f-5e3f61098ae2","enable":true,"trust":"dscp","dscpTag":46}
```

### 使用示例

```bash
# DSCP 模式
acli network pfc create -d '{"domainId":"960d7a90-aad3-4f5c-b57f-5e3f61098ae2","enable":true,"trust":"dscp","dscpTag":46}'

# PCP 模式（业务平面，非 VS）
acli network pfc create -d '{"domainId":"ff348d34-e4ed-40bb-a0ab-0ba24523eda7","enable":true,"trust":"pcp","pcpTag":3}'

# 带 CNP 字段（RoCE 流控场景）
acli network pfc create -d '{"domainId":"960d7a90-aad3-4f5c-b57f-5e3f61098ae2","enable":true,"trust":"dscp","dscpTag":26,"cnpPrio":3,"cnpDscp":48}'
```

### 结果示例

```bash
taskId: host-0050568ecad9:1703505443:0
```
