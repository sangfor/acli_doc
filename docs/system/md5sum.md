---
sidebar_position: 1
---

# md5sum

### 操作概述

计算指定文件的 MD5 校验值（只读）。

### 命令参数

无参数

参数与路径校验说明：`--files0-from=<file>` 指定的是「待计算文件的清单文件」，该清单文件本身必须命中 ls 命令族路径白名单；位置参数指定的待计算文件同样须命中 ls 命令族路径白名单。因 GNU getopt 支持唯一前缀缩写，`--fi <file>` 等缩写形式一样会被识别并按同一规则校验，不会绕过路径白名单校验。

可计算校验值的路径白名单（ls 命令族共用：ls/du/df/md5sum/find 目录列举/校验族，去包含后 40 条，节选）：

```bash
/boot/
/cfs/
/sf/data/
/sf/log/
/sys/class/net/
/run/
```

完整路径白名单清单见 ls 命令族共用路径白名单。

### 使用示例

```bash
acli system md5sum /sf/version
```

### 结果示例

```bash
# acli system md5sum /sf/version
d41d8cd98f00b204e9800998ecf8427e  /sf/version
```
