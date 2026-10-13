---
sidebar_position: 1
---

# turbostat

### 操作概述

查看 CPU 拓扑、频率与功耗统计信息（只读）。命令在 asv-con 容器内执行，最长执行 15 秒。

> 仅 x86/c86 架构支持；arm 架构下执行 `acli system turbostat` 将被拒绝并提示不支持。

### 命令参数

本命令为部分只读命令，选项不设白名单（默认放通），但下列黑名单参数命中即拒绝；不接受子命令/位置参数（未声明任何位置参数键，位置参数一律拒绝）。

禁止参数清单（命中即拒绝，含 GNU 唯一前缀缩写）：

```bash
-o|--out=<file>  将统计结果写入文件，属写操作，拒绝执行；
              因 GNU getopt 支持唯一前缀缩写，--o 开头的写法（--o / --ou）同样命中拒绝
<子命令>         不接受任何位置参数/子命令，命中即拒绝
```

### 使用示例

```bash
acli system turbostat -i 1 --quiet
```

### 结果示例

```bash
# acli system turbostat -i 1 --quiet
CPU     GHz    %Busy   Bzy_MHz   TSC_MHz     CPU%c1    CPU%c6    CPU%c7
-       1.60    25.30     2200      2200       3.20      0.00     71.50
0       1.90    30.00     2200      2200       5.00      0.00     65.00
1       1.30    20.60     2200      2200       1.40      0.00     78.00
```