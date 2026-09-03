---
sidebar_position: 1
---

# hostname

### 操作概述

查看主机名称及域名信息

### 命令参数

```bash
（无参数）             查看完整主机名
-f|--fqdn=flag        查看主机的完全限定域名
-i|--ip-address=flag  查看主机的 IP 地址
-s|--short=flag       查看短主机名
```

### 使用示例

```bash
acli system hostname -f
```

### 结果示例

```bash
host-005056b237a6
```
