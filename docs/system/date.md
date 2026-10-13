---
sidebar_position: 1
---

# date

### 操作概述

date 命令，获取当前系统时间（只读）。

### 命令参数

```bash
-d|--date=string  可选参数，按指定字符串显示时间，示例：acli system date -d "2025-08-27"
-u|--utc=flag     可选参数，以 UTC 时间显示，示例：acli system date -u
+<format>         可选参数，以指定格式输出，示例：acli system date +%Y-%m-%d
```

禁止参数清单（命中即拒绝，含 GNU 唯一前缀缩写）：

```bash
-f|--file=string  禁止参数，从文件读取日期行（批量模式），属文件读取操作，拒绝执行；
                  因 GNU getopt 支持唯一前缀缩写，--f 开头的写法（--f / --fi / --fil）同样命中拒绝；
                  date 没有其它以 f 开头的长选项，故 --f 即为其最短唯一前缀
```

### 使用示例

```bash
acli system date
```

### 结果示例

```bash
Wed Aug 27 14:23:52 GMT-8 2025
```