---
sidebar_position: 1
---

# delete

### 操作概述

为指定网口删除fcoe配置并重启相关服务

### 命令参数

```bash
-i|--interface=string    必要参数，网口名称，示例：eth7
```

### 使用示例

```bash
acli network nic fcoe delete --interface eth7
```

### 结果示例

```bash
fcoe网口配置已删除
```