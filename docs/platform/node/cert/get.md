---
sidebar_position: 1
---

# get

### 操作概述

获取证书的md5值

### 命令参数

```bash
-p|--path=string    必要参数，证书名称，示例：vtp-mysql-ssl.key
```

### 使用示例

```bash
acli platform node cert get -p /sf/cfg/mysql/ssl/vtp-mysql-ssl.key
```

### 结果示例

```bash
017075738f0ba88fe249d61547d6b5b5
```
