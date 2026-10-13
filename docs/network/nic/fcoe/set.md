---
sidebar_position: 1
---

# set

### 操作概述

为指定网口生成fcoe配置并重启相关服务

### 命令参数

```bash
-i|--interface=string    必要参数，网口名称，示例：eth7
```

### 使用示例

```bash
acli network nic fcoe set --interface eth7
```

### 结果示例

```bash
设置成功，fcoe网口配置已生成并生效
```