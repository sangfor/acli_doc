---
sidebar_position: 1
---

# chkconfig

### 操作概述

查看系统服务的运行级别配置（只读）。

### 命令参数

本命令为部分只读命令，采用封闭式参数白名单（仅列举的参数允许，其余拒绝）。

命令格式：

```bash
acli system chkconfig --list [<service>]
acli system chkconfig -l [<service>]
```

支持的参数（白名单内）：

```bash
-l|--list [<service>]  可选参数，列出服务的运行级别配置；省略 <service> 时列出全部服务，
                       指定时仅列出该服务，示例：acli system chkconfig --list sshd
```

写参数禁止清单（命中即拒绝）：

```bash
--level <levels> <service> on/off/reset  修改指定运行级别下服务的启动配置（写）
-a|--add                                 添加服务到 chkconfig 管理（写）
-d|--del                                 从 chkconfig 删除服务（写）
```

### 使用示例

```bash
acli system chkconfig --list sshd
```

### 结果示例

```bash
# acli system chkconfig --list sshd
sshd           	0:off	1:off	2:on	3:on	4:on	5:on	6:off
```
