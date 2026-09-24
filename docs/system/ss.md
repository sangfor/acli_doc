---
sidebar_position: 1
---

# ss

### 操作概述

查看网络套接字统计信息（TCP/UDP 连接等，只读）。

### 命令参数

本命令为部分只读命令，选项不设白名单（默认放通），但下列黑名单参数命中即拒绝。

禁止参数清单（命中即拒绝，含 GNU 唯一前缀缩写）：

```bash
-F|--filter=<file>  从文件读取过滤条件，属文件读取操作，拒绝执行；
                 因 GNU getopt 支持唯一前缀缩写，--fi 开头的写法（--fi / --fil）同样命中拒绝；
                 注意 --family 不受影响（其最短唯一前缀为 --fa）
```

### 使用示例

```bash
acli system ss -tln
```

### 结果示例

```bash
# acli system ss -tln
State    Recv-Q   Send-Q     Local Address:Port      Peer Address:Port
LISTEN   0        128              0.0.0.0:22             0.0.0.0:*
LISTEN   0        128                 [::]:80                [::]:*
```