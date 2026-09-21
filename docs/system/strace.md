---
sidebar_position: 1
---

# strace

### 操作概述

strace 命令，仅支持追踪 acli 命令的系统调用（只读，不修改系统状态）。

### 命令参数

```bash
<command>  位置参数，被追踪的命令，只允许为 acli，示例：acli system strace acli system du /tmp
-c         可选参数，统计各系统调用的时间与次数，示例：acli system strace -c acli system ps
-f         可选参数，追踪子进程，示例：acli system strace -f acli system ps
-e <expr>  可选参数，指定要追踪的系统调用表达式，示例：-e trace=openat
-p <pid>   可选参数，追踪指定进程，示例：-p 1234
-s <size>  可选参数，指定字符串最大显示长度，示例：-s 128
```

禁止参数清单（命中即拒绝，含 GNU 唯一前缀缩写）：

```bash
-o <file>        禁止参数，把跟踪结果写入文件（写操作），拒绝执行；合并写法（-ofile / -fo 等）同样命中
--output=<file>  禁止参数，把跟踪结果写入文件，拒绝执行；
                 因 GNU getopt 支持唯一前缀缩写，--o 开头的写法（--o / --ou / --out）同样命中拒绝
<command>        禁止参数，第一个位置参数不是 acli 时一律拒绝（仅允许追踪 acli 命令）
```

### 使用示例

```bash
acli system strace acli system ps
```

### 结果示例

```bash
# 追踪 acli system ps 命令的系统调用
acli system strace acli system ps
execve("/usr/bin/acli", ["acli", "system", "ps"], 0x7ffd12345678 /* 50 vars */) = 0
brk(NULL)                               = 0x555555556000
arch_prctl(0x3001 /* ARCH_??? */, 0x7ffd12345600) = -1 EINVAL (Invalid argument)
...
```