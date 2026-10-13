---
sidebar_position: 1
---

# du

### 操作概述

统计指定目录或文件的磁盘占用空间（只读）。

### 命令参数

本命令为部分只读命令，选项不设白名单（默认放通），但下列黑名单参数命中即拒绝；位置参数最多 1 个，且路径须命中 ls 命令族共用路径白名单。

禁止参数清单（命中即拒绝，含 GNU 唯一前缀缩写）：

```bash
--files0-from=<file>  从文件读取待统计路径清单，属文件读取操作，拒绝执行；
                      因 GNU getopt 支持唯一前缀缩写，--f 开头的写法
                      （--f / --fi / --fil / --files0）同样命中拒绝
```

可统计的路径白名单（ls 命令族共用：ls/du/df/md5sum/find 目录列举/校验族，去包含后 40 条，节选）：

```bash
/boot/
/cfs/
/dev/
/etc/netplan/
/etc/sysconfig/network-scripts/
/lib/modules/
/mnt/cgroup/cpu
/run/
/sf/data/
/sf/log/
/sys/class/net/
/var/
```

### 使用示例

```bash
acli system du /sf/data/
```

### 结果示例

```bash
# acli system du /sf/data/
6144    /sf/data/local/mock/mc/mc0
1024    /sf/data/local/mock/mc/mc1/dimm2
1024    /sf/data/local/mock/mc/mc1/dimm1
2048    /sf/data/local/mock/mc/mc1/dimm0
5120    /sf/data/local/mock/mc/mc1
12288   /sf/data/local/mock/mc
20480   /sf/data/local/mock
```