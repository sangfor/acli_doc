---
sidebar_position: 1
---

# find

### 操作概述

在指定目录中按条件查找文件（只读）。

### 命令参数

本命令为部分只读命令，采用封闭式参数白名单（仅列举的参数允许，其余拒绝）。

```bash
<path>            必要参数，指定搜索起始目录（仅允许 ls 命令族路径白名单内路径），示例：/sf/data/
-name <pattern>   按文件名匹配（区分大小写）
-iname <pattern>  按文件名匹配（不区分大小写）
-type <type>      按文件类型过滤（f/d/l/b/c/p/s）
-size <size>      按文件大小过滤
-mtime <n>        按修改时间过滤（天）
-mmin <n>         按修改时间过滤（分钟）
-atime <n>        按访问时间过滤（天）
-ctime <n>        按状态变化时间过滤（天）
-maxdepth <n>     最大搜索深度
-mindepth <n>     最小搜索深度
-print            打印匹配结果（默认）
-print0           以 null 分隔打印匹配结果
-ls               以 ls 格式打印匹配结果
-path <pattern>   按完整路径匹配
-perm <mode>      按权限位过滤
-user <name>      按属主过滤
-group <name>     按属组过滤
-newer <file>     比指定文件新
-fstype <type>    按文件系统类型过滤
```

可搜索的路径白名单（ls 命令族共用：ls/du/df/md5sum/find 目录列举/校验族，去包含后 40 条，节选）：

```bash
/boot/
/cfs/
/sf/data/
/sf/log/
/sys/class/net/
/run/
```

写参数禁止清单（命中即拒绝）：

```bash
-exec    在 find 结果上执行命令（写），拒绝执行
-delete  删除匹配的文件（写），拒绝执行
-ok      在 find 结果上交互式执行命令（写），拒绝执行
```

### 使用示例

```bash
acli system find /sf/log/ -name "*error*" -type f
```

### 结果示例

```bash
# acli system find /sf/log/ -name "*error*" -type f
/sf/log/error.log
/sf/log/error.2026-09-08.log
```
