---
sidebar_position: 1
---

# pstack

### 操作概述

读取指定进程的调用栈，用于进程排障。

### 命令参数

命令格式：

```bash
acli system pstack [-n depth] <pid>
acli system pstack -h
acli system pstack --help
```

支持的参数：

本命令采用封闭式参数白名单（未列举即拒绝），无写类参数。

```text
<pid>        查询时指定的进程 ID，须为纯数字，最多 1 个位置参数
-n <层数>    指定调用栈层数
-h|--help    打印帮助信息
```

禁止清单：

层数选项仅放通 `-n`，不提供对应的双横杠长选项。其他选项、非数字 PID 及额外位置参数一律拒绝。

### 使用示例

```bash
acli system pstack 156350
```

进程 ID 需替换为实际待查询的 PID。

### 结果示例

查询进程调用栈：

```text
#0  0x00007f150d6572f0 in nanosleep () from /lib/x86_64-linux-gnu/libc.so.6
#1  0x00007f150d65725a in sleep () from /lib/x86_64-linux-gnu/libc.so.6
#2  0x00007f150e1823b2 in Perl_pp_sleep () from /usr/lib/libperl.so.5.14
#3  0x00007f150e12ec26 in Perl_runops_standard () from /usr/lib/libperl.so.5.14
#4  0x00007f150e0d0755 in perl_run () from /usr/lib/libperl.so.5.14
#5  0x0000000000400f89 in main ()
```

未指定 PID 时：

```text
Usage: pstack <process-id>
```
