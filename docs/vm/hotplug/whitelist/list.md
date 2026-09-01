---
sidebar_position: 5
---

# list

### 操作概述

查询已放通CPU/内存热添加的OS白名单及全局兜底状态

### 命令参数

无参数

### 使用示例

```bash
acli vm hotplug whitelist list
```

### 结果示例

```bash
    Distribution  |Hot-add CPU|Hot-add Memory
    --------------|-----------|--------------
1   Ubuntu 14,64  |√          |×             
2   All Unknown OS|√          |√              
```
