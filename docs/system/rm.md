---
sidebar_position: 1
---

# rm

### 操作概述

rm 命令，限制删除特定目录下的文件（仅允许删除白名单目录内的文件，禁止递归删除）。

### 命令参数

```bash
-f      可选参数，强制删除，不再提示确认，示例：acli system rm -f /tmp/test.log
<path>  位置参数，待删除文件的绝对路径，必须位于允许删除的白名单目录内，
        示例：acli system rm /tmp/test.log
```

禁止参数清单（命中即拒绝，含 GNU 唯一前缀缩写）：

```bash
-r           禁止参数，递归删除（连同目录及其中全部内容一起删除），属高危写操作，拒绝执行
-R           禁止参数，等价于 -r 的递归删除写法，拒绝执行
-rf / -fr    禁止参数，合并短串写法：短选项串中只要出现字符 r 或 R 即命中拒绝
--recursive  禁止参数，递归删除的长选项写法，拒绝执行；
             因 GNU getopt 支持唯一前缀缩写，--r 开头的写法（--r / --re / --rec）同样命中拒绝；
             rm 没有其它以 r 开头的长选项，故 --r 即为其最短唯一前缀
--           禁止参数，选项分隔符：会使 -- 之后的参数不再按选项校验，可能绕过禁止参数判断，拒绝使用
```

除上述禁止参数外，位置参数只能是以绝对路径给出的白名单目录内的文件；`/sf/data/local/acli/tmp` 目录禁止删除。

### 使用示例

```bash
acli system rm /var/spool/test.log
```

### 结果示例

下面示例给出一条不在白名单目录内的路径，命令经确认后被拒绝，并列出允许删除的目录清单：

```bash
# acli system rm /var/spool/test.log
Are you sure you want to execute the operation? (y[es]/n[o]):请使用绝对路径，仅能删除如下目录下的文件：
/sf/log/
/run/
/var/log/
/tmp/
/sf/data/
/sf/cfg/
/sf/vs/vscfg/
```