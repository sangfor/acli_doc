---
sidebar_position: 1
---

# dmesg

### 操作概述

查看内核环形缓冲区日志（只读）。

### 命令参数

本命令为部分只读命令，选项不设白名单（默认放通），但下列黑名单参数命中即拒绝；不接受位置参数（未声明任何位置参数键，位置参数一律拒绝）。

禁止参数清单（命中即拒绝，含 GNU 唯一前缀缩写）：

```bash
-F <file>      从文件读取日志，属文件读取操作（绕过内核环形缓冲区只读语义），拒绝执行
--file=<file>  从文件读取日志，属文件读取操作（绕过内核环形缓冲区只读语义），拒绝执行；
               因 GNU getopt 支持唯一前缀缩写，--fi 开头的写法（--fi / --fil）同样命中拒绝；
               注意 --facility / --follow / --force-prefix 不受影响（其最短唯一前缀为 --fa / --fo）
```

### 使用示例

```bash
acli system dmesg -T --level=err
```

### 结果示例

```bash
# acli system dmesg -T --level=err
[Tue Sep  8 10:30:01 2026] EDAC sbridge: ECC errors on CPU0
[Tue Sep  8 10:31:12 2026] megaraid_sas 0000:03:00.0: resetting adapter
```