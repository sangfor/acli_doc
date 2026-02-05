---
sidebar_position: 1
---

# list

### 操作概述

展示所有的acli命令

### 命令参数

```bash
-c|--command-filter=string        仅显示名称中包含指定字符串的命令，示例：list
-d|--description-filter=string    仅显示描述中包含指定字符串的命令，示例：acli命令
-n|--namespace-filter=string      仅显示命名空间中包含指定字符串的命令，示例：command
```

### 使用示例

```bash
# 查询所有命令信息
acli command list

# 查询命名空间包含"host"的命令
acli command list -n host
```

### 结果示例

```bash
命名空间                                      命令         描述
--------------------------------------------  -----------  ------------------------------------------
hardware.disk.smartinfo                       get          获取硬盘的所有SMART信息
hardware.cpu.info                             get          获取硬件中CPU信息
......
```
