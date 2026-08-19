---
sidebar_position: 1
---

# convert

### 操作概述

将普通云主机转换为占位云主机，把复制存储中的普通云主机 VM 转成占位 VM，占位存储由用户指定，调用 vmman convert-to-placeholder 接口下发转换指令。

### 命令参数

```bash
-v|--vm-id=string                    必要参数，源虚拟机id，示例：6882173957870
-p|--placeholder-datastore-id=string 必要参数，占位存储id，示例：1SANGFOR_ASAN-003-5171-4ac2-b777-62d94ef8fb7b
```

### 使用示例

```bash
acli vm dr placeholder convert -v 6882173957870 -p 1SANGFOR_ASAN-003-5171-4ac2-b777-62d94ef8fb7b
```

### 结果示例

```bash
# 成功
转换占位虚拟机指令已下发
任务ID: <taskID>
```
