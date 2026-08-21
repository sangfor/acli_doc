---
sidebar_position: 5
---

# delete

### 操作概述

删除优先级流控(PFC)配置（异步任务，返回 taskId）

### 命令参数

```bash
-i|--flowcontrol-id=string    必要参数，流控配置ID（UUID），用于定位待删除的流控配置
```

### 使用示例

```bash
# 先 list 拿到 id
acli network pfc list -d 960d7a90-aad3-4f5c-b57f-5e3f61098ae2

# 删除
acli network pfc delete -i 215613f8-4ee3-4d56-a602-d05fe9cd484c
```

### 结果示例

```bash
taskId: host-0050568ecad9:1703505480:2
```
