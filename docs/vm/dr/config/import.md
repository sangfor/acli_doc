---
sidebar_position: 1
---

# import

### 操作概述

从复制存储导入虚拟机配置，读取源 VM 的 conf，按用户下发的存储映射生成磁盘映射，调用 vmman import-config 接口下发导入指令。

### 命令参数

```bash
-s|--source-vm-id=string        必要参数，源虚拟机id，示例：6882173957870
-c|--cfgstorage-id=string       必要参数，源虚拟机配置的存储id，示例：1SANGFOR_ASAN-003-5171-4ac2-b777-62d94ef8fb7b
-t|--target-vm-id=string        目标虚拟机id，可选，示例：9876543210
-m|--storage-map=string         必要参数，存储映射，格式 src=<源存储ID>,dst=<目标存储ID>，多组映射以分号分隔，示例：src=1SANGFOR_ASAN-003-5171-4ac2-b777-62d94ef8fb7b,dst=1SANGFOR_ASAN-003-5171-4ac2-b777-62d94ef8fb7c;src=pool_a,dst=pool_b
```

### 使用示例

```bash
acli vm dr config import -s 6882173957870 -c 1SANGFOR_ASAN-003-5171-4ac2-b777-62d94ef8fb7b -m src=1SANGFOR_ASAN-003-5171-4ac2-b777-62d94ef8fb7b,dst=1SANGFOR_ASAN-003-5171-4ac2-b777-62d94ef8fb7c
```

### 结果示例

```bash
# 成功
导入虚拟机配置指令已下发
任务ID: <taskID>
```