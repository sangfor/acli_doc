---
sidebar_position: 1
---
  
# set

### 操作概述

设置报表数据配置
  
### 命令参数

```bash
  -s|--storage-id=string              必要参数，指定存储id，示例：36000c29a3c9419c600cdb98b5f823744_005056893c9d
  -f|--force=integer                  强制修改（忽略存储报错），示例：1 强制，0 不强制
```
  
### 使用示例

```bash
acli platform datareport set -s 019de1b3f4507b6991e610e0ed77c9df -f 1
```
  
### 结果示例

```bash
host-0050568eb53e:2422079:1779351636:6928791085320
```
