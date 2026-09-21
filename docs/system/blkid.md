---
sidebar_position: 1
---

# blkid

### 操作概述

查询块设备的 UUID、文件系统类型及其他属性信息（只读）。

### 命令参数

命令格式：

```bash
acli system blkid [<dev>]
```

本命令为部分只读命令，选项不设白名单（默认放通），但下列黑名单参数命中即拒绝。

禁止参数清单（命中即拒绝，含 GNU 唯一前缀缩写）：

```bash
-c|--cache-file=string  写缓存文件，属于写操作，拒绝执行；
                        因 GNU getopt 支持唯一前缀缩写，--c 开头的写法（如 --c / --ca）
                        同样命中拒绝
-w|--write=string       将设备缓存写入指定文件，属于写操作，拒绝执行；
                        因 GNU getopt 支持唯一前缀缩写，--w 开头的写法（如 --w）
                        同样命中拒绝
```

可查询的路径白名单（dev 命令族路径白名单，仅 1 条，即 /dev/ 目录）：

```bash
/dev/  （块设备目录，支持前缀匹配，如 /dev/sda）
```

### 使用示例

```bash
acli system blkid /dev/sda
```

### 结果示例

```bash
# acli system blkid /dev/sda
/dev/sda: UUID="1a2b3c4d-5e6f-7890-abcd-ef1234567890" TYPE="ext4" PARTUUID="12345678-01"
```
